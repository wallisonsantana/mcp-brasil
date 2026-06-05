#!/usr/bin/env python3
"""
Extrai GASTOS DE CAMPANHA (total + digital) por candidato a Deputado Federal
do Tocantins direto dos DADOS ABERTOS do TSE (prestação de contas).

POR QUE ESTE SCRIPT EXISTE
--------------------------
A API DivulgaCandContas (usada pelo mcp-brasil em src/mcp_brasil/data/tse/)
devolve apenas TOTAIS consolidados (total de despesas, fundo, etc.) — NÃO o
detalhamento por categoria. O gasto com INTERNET / IMPULSIONAMENTO / REDES
SOCIAIS / TRÁFEGO só existe no arquivo de "despesas contratadas" dos Dados
Abertos. Este script baixa esse arquivo e faz a quebra por categoria.

IMPORTANTE: rode este script numa rede com acesso ao TSE (sua máquina).
No ambiente do Claude Code Web o egress ao cdn.tse.jus.br está bloqueado.

USO
---
    python extrair_gastos_tse.py            # 2022, Deputado Federal, TO
    python extrair_gastos_tse.py --ano 2022 --uf TO --cargo "DEPUTADO FEDERAL"

Sem dependências externas (só biblioteca padrão). Python 3.9+.
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
import urllib.request
import zipfile
from collections import defaultdict

# URL oficial dos Dados Abertos — prestação de contas de candidatos.
ZIP_URL = (
    "https://cdn.tse.jus.br/estatistica/sead/odsele/prestacao_contas/"
    "prestacao_de_contas_eleitorais_candidatos_{ano}.zip"
)

# Categorias (DS_ORIGEM_DESPESA / DS_TIPO_DESPESA) consideradas "digital".
# O TSE muda levemente os rótulos por ano; casamos por palavra-chave.
PALAVRAS_DIGITAL = (
    "impulsion",      # impulsionamento de conteúdo
    "internet",       # criação/inclusão de páginas na internet
    "rede social",
    "redes sociais",
    "site",
    "sítio",
    "digital",
    "marketing eletr",
    "blog",
)

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"


def baixar_zip(ano: int) -> zipfile.ZipFile:
    url = ZIP_URL.format(ano=ano)
    print(f"[1/4] Baixando {url} ...", file=sys.stderr)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read()
    print(f"      OK ({len(data)/1e6:.1f} MB)", file=sys.stderr)
    return zipfile.ZipFile(io.BytesIO(data))


def achar_arquivo_despesas(zf: zipfile.ZipFile, uf: str) -> str:
    """Encontra o CSV de despesas contratadas (por UF ou BRASIL)."""
    nomes = zf.namelist()
    # Preferência: arquivo específico da UF
    for nome in nomes:
        n = nome.lower()
        if "despesas_contratadas" in n and f"_{uf.lower()}." in n:
            return nome
    # Alternativa: arquivo nacional (filtra SG_UF depois)
    for nome in nomes:
        n = nome.lower()
        if "despesas_contratadas" in n and "brasil" in n:
            return nome
    raise FileNotFoundError(
        "Não achei 'despesas_contratadas...'. Arquivos no zip:\n  "
        + "\n  ".join(nomes)
    )


def is_digital(texto: str) -> bool:
    t = (texto or "").lower()
    return any(p in t for p in PALAVRAS_DIGITAL)


def col(row: dict, *nomes: str) -> str:
    """Pega a 1ª coluna existente (nomes de coluna mudam por ano)."""
    for n in nomes:
        if n in row and row[n] not in (None, ""):
            return row[n]
    return ""


def brl(v: float) -> str:
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ano", type=int, default=2022)
    ap.add_argument("--uf", default="TO")
    ap.add_argument("--cargo", default="DEPUTADO FEDERAL")
    args = ap.parse_args()

    zf = baixar_zip(args.ano)
    nome_csv = achar_arquivo_despesas(zf, args.uf)
    print(f"[2/4] Lendo {nome_csv}", file=sys.stderr)

    total_cand: dict[str, float] = defaultdict(float)
    digital_cand: dict[str, float] = defaultdict(float)
    partido_cand: dict[str, str] = {}
    categorias_digital: dict[str, float] = defaultdict(float)

    with zf.open(nome_csv) as fh:
        # Dados Abertos do TSE: latin-1, separador ';'
        text = io.TextIOWrapper(fh, encoding="latin-1", newline="")
        reader = csv.DictReader(text, delimiter=";")
        for row in reader:
            uf = col(row, "SG_UF", "SG_UF_SUP")
            if uf and uf.upper() != args.uf.upper():
                continue
            cargo = col(row, "DS_CARGO", "DS_CARGO_CANDIDATO")
            if args.cargo.upper() not in (cargo or "").upper():
                continue

            nome = col(row, "NM_CANDIDATO", "NM_URNA_CANDIDATO") or "—"
            partido = col(row, "SG_PARTIDO", "NR_PARTIDO")
            categoria = col(
                row, "DS_ORIGEM_DESPESA", "DS_TIPO_DESPESA", "DS_DESPESA"
            )
            valor_raw = col(row, "VR_DESPESA_CONTRATADA", "VR_DESPESA", "VR_PAGAMENTO")
            try:
                valor = float(valor_raw.replace(".", "").replace(",", "."))
            except ValueError:
                continue

            partido_cand[nome] = partido
            total_cand[nome] += valor
            if is_digital(categoria):
                digital_cand[nome] += valor
                categorias_digital[categoria.strip()] += valor

    print(f"[3/4] {len(total_cand)} candidatos a {args.cargo} em {args.uf}\n",
          file=sys.stderr)

    # Ranking por gasto total
    ordenado = sorted(total_cand.items(), key=lambda kv: kv[1], reverse=True)
    print(f"=== GASTO DE CAMPANHA — {args.cargo} / {args.uf} / {args.ano} ===\n")
    print(f"{'#':>2}  {'Candidato':30} {'Part.':6} {'Total':>16} "
          f"{'Digital':>14} {'% dig':>6}")
    print("-" * 80)
    for i, (nome, tot) in enumerate(ordenado, 1):
        dig = digital_cand.get(nome, 0.0)
        pct = (dig / tot * 100) if tot else 0
        print(f"{i:>2}  {nome[:30]:30} {partido_cand.get(nome,''):6} "
              f"{brl(tot):>16} {brl(dig):>14} {pct:>5.1f}%")

    print("\n[4/4] Categorias DIGITAIS encontradas (estado todo):")
    for cat, v in sorted(categorias_digital.items(), key=lambda kv: -kv[1]):
        print(f"   {brl(v):>16}  {cat}")

    print(
        "\nNOTA: para cruzar com VOTOS, baixe também "
        f"'votacao_candidato_munzona_{args.ano}_{args.uf}.zip' nos Dados Abertos "
        "e some QT_VOTOS_NOMINAIS por SQ_CANDIDATO. Ou use a API DivulgaCandContas "
        "(src/mcp_brasil/data/tse/client.py -> buscar_candidato) para total_votos."
    )


if __name__ == "__main__":
    main()
