# Briefing de Coleta — Dados Financeiros e Eleitorais (TO / Deputado Federal)

**Para: agente autônomo com acesso à internet**
**Objetivo:** preencher as lacunas financeiras que o ambiente atual não conseguiu (egress ao TSE bloqueado). Tudo que está aqui é **coletável publicamente e de graça**.

> Regra de ouro: **registrar a URL e a data de coleta de cada número.** Quando houver divergência entre fontes, prevalece o **TSE** (DivulgaCandContas / Dados Abertos). Não estimar — se não achar, marcar "não encontrado".

---

## PARTE 1 — O QUE PRECISA SER COLETADO (campos exatos)

### Alvo A — Ricardo Ayres (Republicanos) · eleição 2022 · **PRIORIDADE MÁXIMA**
Coletar, para a campanha de Deputado Federal/2022:
1. **Total arrecadado (receita)** — R$.
2. **Composição da receita:** (a) Fundo Especial/FEFC; (b) Fundo Partidário; (c) Recursos próprios; (d) Doações de pessoas físicas; (e) Doações de outros candidatos/partidos.
3. **Total de despesas (gasto total)** — R$.
4. **Despesa por categoria**, com destaque para as DIGITAIS:
   - Impulsionamento de conteúdos (**= tráfego pago**);
   - Criação/manutenção de páginas na internet e redes sociais;
   - Produção de conteúdo/vídeo para internet;
   - (e as demais: pessoal, combustível, material impresso, publicidade, etc.).
5. **Votação nominal total** (já temos: 45.880 — confirmar) **e votos por município** (top 10).
6. **Limite de gastos declarado** e se as contas foram **aprovadas**.
7. **Custo por voto** (calcular: gasto total ÷ votos).
8. **% do orçamento gasto em digital** (calcular).

### Alvo B — Comparáveis evangélicos eleitos em 2022 (mesmo perfil da Rosilene)
Mesmos 8 itens acima para:
- **Filipe Martins (PL)** — 36.293 votos;
- **Eli Borges (PL)** — 35.171 votos.
*(São o melhor espelho: evangélicos que se elegeram na faixa de ~35 mil votos.)*

### Alvo C — Benchmark dos 8 eleitos (2022)
Para **cada um dos 8** (Toinho Andrade, Vicentinho Júnior, Alexandre Guimarães, Carlos Gaguim, Ricardo Ayres, Filipe Martins, Eli Borges, Lázaro Botelho): **gasto total, % digital e custo por voto.** Objetivo: montar a tabela "votos × gasto × % digital × custo/voto" dos eleitos.

### Alvo D — Rosilene Martins · histórico próprio (a LINHA DE BASE — crítico)
1. **2022 — Deputada Estadual:** partido, **votos nominais exatos** (a imprensa cita "~5 mil" — confirmar), votos por município, **gasto total e % digital**, resultado (suplente?).
2. **2024 — Vereadora de Palmas (Republicanos, nº 10777):** **votos nominais exatos**, **gasto total e % digital**, resultado.
*(Sem esses dois números, nenhuma projeção dela é confiável.)*

### Alvo E — Fábio Vaz · base municipal prévia
- **Prefeito de Palmeirópolis:** votos nas eleições que venceu (2012? 2016?), e gasto se disponível. Dimensiona a base real que ele leva para a federal.

### Alvo F — FEFC 2026 (quando publicado)
- Quanto o **Republicanos nacional** recebeu do Fundo Eleitoral 2026 e, se houver, **quanto o diretório TO** deve distribuir. (Já temos o total nacional ~R$ 4,9 bi; falta o recorte do partido.)

---

## PARTE 2 — ONDE BUSCAR E O CAMINHO EXATO

### Fonte 1 — DivulgaCandContas (TSE) · **fonte primária para finanças**
**Site (app web):** `https://divulgacandcontas.tse.jus.br/divulga/`
Caminho de clique:
1. Selecionar **Eleição: "Eleições Gerais Federais 2022"**.
2. **UF: Tocantins** → **Cargo: Deputado Federal**.
3. Buscar o candidato pelo nome → abrir a ficha.
4. Aba **"Prestação de Contas"** → ver **Receitas** (com fontes) e **Despesas** (com categorias).
5. Baixar o **PDF/relatório** da prestação (tem o detalhamento por rubrica, incluindo impulsionamento/internet).

**API REST (mais rápido para o agente — devolve JSON):** base
`https://divulgacandcontas.tse.jus.br/divulga/rest/v1`
- Listar anos: `GET /eleicao/anos-eleitorais`
- Listar eleições ordinárias (pegar o `eleicao_id` de 2022): `GET /eleicao/ordinarias`
- Listar candidatos do cargo: `GET /candidatura/listar/2022/{municipio}/{eleicao_id}/6/candidatos` (cargo **6 = Dep. Federal**; `{municipio}` para cargo estadual = código de abrangência da UF — descobrir via o app).
- Ficha do candidato (tem `totalVotos` e `gastoCampanha`): `GET /candidatura/buscar/2022/{municipio}/{eleicao_id}/candidato/{candidato_id}`
- Prestação de contas (receita/despesa consolidada): `GET /prestador/consulta/{eleicao_id}/2022/{municipio}/6/90/90/{candidato_id}`
> ⚠️ A API costuma retornar **403 sem cabeçalhos de navegador**. Enviar `User-Agent` de browser + `Referer: https://divulgacandcontas.tse.jus.br/`. Se persistir, usar a Fonte 2 (Dados Abertos), que é a forma definitiva.

### Fonte 2 — Dados Abertos do TSE · **definitiva para gasto digital por categoria**
**Portal:** `https://dadosabertos.tse.jus.br/` (e CDN `https://cdn.tse.jus.br/estatistica/sead/odsele/`)
Arquivos a baixar (2022):
- **Prestação de contas (receitas + despesas por categoria):**
  `https://cdn.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_de_contas_eleitorais_candidatos_2022.zip`
  → dentro: `receitas_candidatos_2022_TO.csv` e `despesas_contratadas_candidatos_2022_TO.csv`.
- **Votação por candidato/município:**
  `https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2022.zip`
  → `votacao_candidato_munzona_2022_TO.csv` (somar `QT_VOTOS_NOMINAIS` por `SQ_CANDIDATO`).
- **Cadastro de candidatos (liga nome ↔ SQ_CANDIDATO ↔ partido):**
  `https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2022.zip` → `consulta_cand_2022_TO.csv`.
- **Para a Rosilene 2024 (estadual é 2022; vereadora é 2024):** trocar "2022" por "2024" nos mesmos caminhos (votação e prestação) e usar o arquivo `_TO.csv`.

> Formato dos CSV: encoding **latin-1**, separador **`;`**. O script `extrair_gastos_tse.py` (nesta pasta) já faz o download, o filtro por cargo e a quebra digital — **mande o agente rodá-lo** e, se quiser, ampliar para receitas e votos.

**Dicionário de campos (despesas_contratadas):**
- `NM_CANDIDATO`, `SQ_CANDIDATO`, `SG_PARTIDO`, `DS_CARGO`
- `DS_ORIGEM_DESPESA` → **a categoria** (procurar: "impulsionamento", "internet", "redes sociais", "criação...páginas")
- `VR_DESPESA_CONTRATADA` → **o valor**
- `NM_FORNECEDOR` → quem recebeu (útil p/ ver agências de tráfego)

**Dicionário (receitas):** `VR_RECEITA`, `DS_FONTE_RECEITA` / `DS_ORIGEM_RECEITA` (Fundo Especial, Fundo Partidário, Recursos próprios, Doações).

### Fonte 3 — Repositório de Dados Eleitorais (TSE, legado)
`https://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1`
Mesmos datasets em outro layout — usar como alternativa se a CDN falhar.

### Fonte 4 — Câmara dos Deputados (só para o Ricardo Ayres, mandato)
`https://www.camara.leg.br/deputados/` → ficha do Ayres: gabinete, comissões, **cota parlamentar (CEAP)** e gastos de gabinete — útil para dimensionar a estrutura institucional que ele tem (e a Rosilene não tem).

### Fonte 5 — Agregadores/jornalismo (atalho e validação cruzada)
- **Quem com Quem** — `https://quemcomquem.com.br` (financiamento de campanha por candidato).
- **Ranking dos Políticos** — `https://www.rankingdospoliticos.com.br`.
- **Especiais G1 Eleições 2022** — página por candidato com prestação (buscar "g1 eleições 2022 Ricardo Ayres Tocantins").
- **Poder360 / Metrópoles / JOTA / Congresso em Foco** — reportagens de "quanto gastou cada eleito".
- **Transparência Brasil / "As Claras"** — financiamento histórico.
- **Pindograma** — análises com dados de gasto/voto.

### Fonte 6 — Redes sociais (para o digital da Rosilene e dos puxadores)
- Instagram/Facebook/YouTube/TikTok de cada um: **nº de seguidores, engajamento, frequência** — para comparar o ativo orgânico (onde a Rosilene tende a liderar).
- Biblioteca de Anúncios da Meta (`https://www.facebook.com/ads/library/`, filtro "Anúncios sobre temas sociais, eleições ou política", país Brasil): mostra **quem está impulsionando e quanto** — ótimo para ver o tráfego pago dos concorrentes em tempo real.

---

## PARTE 3 — ENTREGÁVEL ESPERADO DO AGENTE

1. **Tabela mestra dos 8 eleitos (2022):** Nome | Partido | Votos | Receita total | % Fundo (FEFC+partidário) | Despesa total | **Gasto digital R$** | **% digital** | Custo/voto.
2. **Ficha detalhada de 3 alvos** (Ricardo Ayres, Filipe Martins, Eli Borges): receita por fonte + despesa por categoria (todas as rubricas), top municípios de votação.
3. **Linha de base da Rosilene:** votos e gasto (2022 estadual + 2024 vereadora), com % digital.
4. **Mapa de eficiência:** para Ayres/Filipe/Eli, os municípios onde concentraram votos (achar brechas geográficas para a Rosilene).
5. **Meta da Biblioteca de Anúncios Meta:** quem dos pré-candidatos 2026 já roda tráfego e volume aproximado.
6. **FEFC 2026:** valor do Republicanos nacional (e TO se houver).
7. Cada número com **URL + data**. Lacunas marcadas como "não encontrado".

---

## PARTE 4 — CHECKLIST RÁPIDO (para colar no pedido do agente)

- [ ] Ricardo Ayres 2022: receita, fontes, despesa total, **gasto digital R$ e %**, votos/município, custo/voto, contas aprovadas?
- [ ] Filipe Martins 2022: idem.
- [ ] Eli Borges 2022: idem.
- [ ] Demais 5 eleitos: gasto total, % digital, custo/voto.
- [ ] Rosilene 2022 (estadual): partido, votos exatos, gasto, % digital, resultado.
- [ ] Rosilene 2024 (vereadora Palmas): votos exatos, gasto, % digital, resultado.
- [ ] Fábio Vaz: votação como prefeito de Palmeirópolis (ano e votos).
- [ ] FEFC 2026: cota do Republicanos.
- [ ] Meta Ad Library: tráfego pago atual dos pré-candidatos 2026 do Republicanos.
- [ ] Redes sociais: seguidores/engajamento de Ayres, Cel. Barbosa, Atos, Fábio, Rosilene.

> **Dica final:** o caminho de **menor atrito** é a **Fonte 2 (Dados Abertos + script `extrair_gastos_tse.py`)** — um download resolve gasto e digital de TODOS os candidatos de uma vez. A API e os agregadores servem para **validar e completar** (votos por município, fontes de receita, redes).
