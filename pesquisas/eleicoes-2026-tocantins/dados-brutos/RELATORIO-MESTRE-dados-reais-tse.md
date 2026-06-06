# Relatório Mestre — Dados Financeiros e Eleitorais (TO / Deputado Federal)

**Projeto:** viabilidade da candidatura de Rosilene Martins a Deputada Federal/TO em 2026
**Data da coleta:** 05/06/2026
**Fonte primária (finanças, votos):** TSE — Dados Abertos (CDN `cdn.tse.jus.br/estatistica/sead/odsele/`), arquivos `consulta_cand`, `prestacao_de_contas_eleitorais_candidatos` e `votacao_candidato_munzona`, recortes `_TO`, eleições 2022/2024/2016.
**Método:** ligação nome de urna → `SQ_CANDIDATO` via cadastro; soma de `VR_DESPESA_CONTRATADA` por `DS_ORIGEM_DESPESA`, `VR_RECEITA` por origem, e `QT_VOTOS_NOMINAIS` por município. Script reprodutível: `extrair_gastos_tse.py` (dados brutos em `resultados_tse.json`).

> **Nota metodológica sobre "digital":** o número de **tráfego pago** usa estritamente a rubrica TSE **"Despesa com Impulsionamento de Conteúdos"** (Meta/Google). A rubrica "Produção de programas de rádio, televisão ou **vídeo**" **não** é contada como digital (é broadcast), para não inflar o número.

---

## 1. TABELA MESTRA — Os 8 eleitos a Deputado Federal/TO (2022)

| # | Nome (urna) | Partido | Votos | Receita (R$) | % Recursos partidários¹ | Despesa total (R$) | Tráfego pago (R$) | % tráfego | Custo/voto (R$) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Toinho Andrade | Republicanos | 63.813 | 888.491 | 79,3% | 846.088 | **0** | 0,0% | 13,26 |
| 2 | Vicentinho Júnior | PP | 55.292 | 2.870.000 | 91,3% | 2.609.510 | 2.049 | 0,1% | 47,20 |
| 3 | Alexandre Guimarães | Republicanos | 54.703 | 979.543 | 61,6% | 925.777 | **0** | 0,0% | 16,92 |
| 4 | Carlos Gaguim | União | 52.203 | 2.345.142 | 98,9% | 2.199.647 | 30.000 | 1,4% | 42,14 |
| 5 | Ricardo Ayres | Republicanos | 45.880 | 850.731 | 71,1% | 774.815 | 10.000 | 1,3% | 16,89 |
| 6 | Filipe Martins | PL | 36.293 | 899.080 | 55,7% | 785.493 | **39.500** | 5,0% | 21,64 |
| 7 | Eli Borges | PL | 35.171 | 2.016.740 | 99,2% | 1.999.950 | **0** | 0,0% | 56,86 |
| 8 | Lázaro Botelho | PP | 13.668 | 2.681.200 | 99,2% | 2.659.934 | **0** | 0,0% | 194,61 |

¹ "Recursos de partido político" no extrato 2022 = FEFC (Fundo Eleitoral) + Fundo Partidário somados (o TSE não separa as duas rubricas neste recorte).

**Leituras-chave da tabela:**
- **O tráfego pago NÃO decide a eleição federal no TO.** O campeão de impulsionamento entre os eleitos é Filipe Martins (R$39,5 mil = 5%). Cinco dos oito eleitos gastaram **R$0 ou ~R$2 mil** em impulsionamento. Eli Borges (35 mil votos) e Lázaro Botelho gastaram **zero**.
- **Custo por voto despenca com base física/orgânica:** os mais baratos (Toinho R$13, Ayres R$16,9, Alexandre R$16,9) são os de menor gasto absoluto e zero/quase-zero tráfego pago — venceram por capilaridade e estrutura.
- **Lázaro Botelho** é o outlier: R$2,66 mi para 13.668 votos (R$194/voto), eleito "por média" (puxado pela coligação), não por votação própria.
- **Quem dá o melhor espelho da Rosilene** (evangélicos, ~35 mil votos): **Filipe Martins (PL, 36.293)** e **Eli Borges (PL, 35.171)** — detalhados na seção 3.

---

## 2. FICHAS DETALHADAS — 3 alvos prioritários

### 2.1 Ricardo Ayres (Republicanos) — ALVO PRIORITÁRIO · 45.880 votos · ELEITO por média
- **Nome civil:** Ricardo Ayres de Carvalho · nº 1000 · SQ 270001654164
- **Receita total:** R$ 850.731,25
  - Recursos de partido político: R$ 604.531,25 (71,1%)
  - Pessoas físicas: R$ 228.600,00 (26,9%)
  - Recursos próprios: R$ 10.000,00 · Outros candidatos: R$ 7.600,00
- **Despesa total:** R$ 774.814,70
- **Tráfego pago (impulsionamento):** R$ 10.000,00 (1,29%) — fornecedor: **Facebook Serviços Online do Brasil**
- **Principais despesas:** Material impresso R$193.136 · Militância/mobilização de rua R$179.345 · Locação de veículos R$154.250 · Combustível R$66.881 · Adesivos R$48.870
- **Custo por voto:** R$ 16,89
- **Top municípios:** Palmas (6.124), Porto Nacional (3.762), Miracema (1.972), Axixá (1.844), Dianópolis (1.546), Gurupi (1.336), Palmeirópolis (986), Guaraí (942), Taipas (862), Augustinópolis (823)
- **Perfil de campanha:** "voto pulverizado" e capilar (boa distribuição entre médias cidades), baixo digital, forte rua/impресso. É o modelo mais barato e eficiente entre os caros.

### 2.2 Filipe Martins (PL) — ESPELHO EVANGÉLICO Nº 1 · 36.293 votos · ELEITO por média
- **Nome civil:** Filipe Martins dos Santos · nº 2222 · SQ 270001643553
- **Receita total:** R$ 899.080,00
  - Recursos de partido político: R$ 500.840,00 (55,7%)
  - Recursos próprios: R$ 299.040,00 (33,3%) · Pessoas físicas: R$ 83.300 · Outros candidatos: R$ 15.900
- **Despesa total:** R$ 785.492,57
- **Tráfego pago:** R$ 39.500,00 (5,03%) — **o maior % entre os 8 eleitos** — fornecedor Facebook. (+R$15 mil em produção de vídeo, contabilizada à parte.)
- **Principais despesas:** Militância/mobilização R$265.300 · Material impresso R$163.770 · Adesivos R$155.158 · Pessoal R$73.500 · Combustível R$49.678
- **Custo por voto:** R$ 21,64
- **Top municípios:** **Palmas (13.051 — fortíssima concentração na capital)**, Gurupi (2.436), Araguaína (1.573), Formoso do Araguaia (1.453), Porto Nacional (1.363), Paraíso (1.239), Araguatins (969), Figueirópolis (796), Guaraí (538), Colinas (494)
- **Perfil:** voto MUITO concentrado em Palmas (36% do total na capital). Base urbana/bolsonarista. É o eleito que mais usou digital — e ainda assim só 5%.

### 2.3 Eli Borges (PL) — ESPELHO EVANGÉLICO Nº 2 · 35.171 votos · ELEITO por média
- **Nome civil:** Eli Dias Borges · nº 2200 · SQ 270001643551
- **Receita total:** R$ 2.016.740,00 — **quase 100% partido** (R$ 2.000.840 = 99,2%; R$15.900 de outros candidatos)
- **Despesa total:** R$ 1.999.950,32
- **Tráfego pago:** **R$ 0,00 (0%)** — não declarou impulsionamento
- **Principais despesas:** **Doações a outros candidatos/partidos R$698.300** (!!) · Militância/mobilização R$581.600 · Locação de veículos R$265.350 · Adesivos R$137.930 · Material impresso R$126.950 · Combustível R$83.701
- **Custo por voto:** R$ 56,86 (alto)
- **Top municípios:** **Palmas (10.304)**, Araguaína (2.014), Gurupi (1.822), Paraíso (1.457), Sandolândia (1.207), Guaraí (1.080), Porto Nacional (972), Colméia (928), Palmeirópolis (881), Ponte Alta (845)
- **Perfil:** pastor da CIADSETA (mesma igreja da Rosilene), campanha cara e financiada quase só por fundo partidário, **zero digital**, e usou R$698 mil para irrigar aliados — modelo "máquina/igreja", não modelo de mídia. Voto concentrado em Palmas + capilaridade pastoral.

> **Insight para a Rosilene:** Eli Borges é o caso mais importante. Ele é da **mesma igreja (CIADSETA)** e venceu com 35 mil votos **sem nenhum tráfego pago**, no modelo "rede de igrejas + fundo partidário". A sucessão dele abre uma disputa familiar/interna pela vaga (ver fontes de imprensa). A Rosilene compete exatamente nesse espaço.

---

## 3. LINHA DE BASE DA ROSILENE (crítico)

> ⚠️ **Correção factual importante vs. o briefing:** os dados oficiais do TSE mostram um histórico **mais frágil** do que o pressuposto. Confirmar antes de qualquer projeção.

### 3.1 Rosilene 2022 — Deputada **Estadual** (não federal)
- **Nome civil:** Rosilene Pereira de Sousa Cruz · **Partido: PTB** (não Republicanos em 2022) · nº 14522 · SQ 270001675938
- **Votos nominais:** **4.398** (a imprensa citava "~5 mil" — o número exato é **4.398**)
- **Resultado:** **NÃO ELEITO** (não foi suplente classificado)
- **Receita:** R$ 93.566,66 (partido R$51.667 · outros candidatos R$25.000 · PF R$12.000 · próprios R$4.900)
- **Despesa total:** R$ 64.862,70 · **Tráfego pago:** R$ 3.000 (4,63%, Facebook)
- **Custo por voto:** R$ 14,75
- **Top municípios:** **Palmas (1.751)**, Guaraí (619), Porto Nacional (191), Colinas (170), Araguaína (142), Miranorte (88)
- *Voto concentrado em Palmas + Guaraí; base estreita.*

### 3.2 Rosilene 2024 — Vereadora de Palmas (Republicanos, nº 10777)
- **Mesma pessoa** · Partido: **Republicanos** · SQ 270002190007
- **Votos nominais:** **657** (só em Palmas)
- **Resultado:** **SUPLENTE** (NÃO eleita vereadora)
- **Receita:** R$ 136.033,32 (partido R$133.033 · PF R$3.000)
- **Despesa total:** R$ 119.756,50 · **Tráfego pago:** R$ 2.200 (1,84%)
- **Custo por voto:** **R$ 182,28** (altíssimo — gastou R$119 mil para 657 votos)

> **Implicação estratégica honesta:** a base eleitoral própria comprovada da Rosilene é **pequena e em queda** (4.398 votos estaduais em 2022 → 657 votos municipais em 2024, ambas as vezes sem se eleger). A tese de que ela "salta" para ~35 mil votos federais (faixa Filipe/Eli) **não se sustenta no histórico individual** — depende inteiramente de um ativo que os números do TSE não medem: a **transferência da rede CIADSETA / capital orgânico evangélico**. Esse é o ponto que precisa ser comprovado (seguidores, alcance, apoio formal de lideranças), porque a urna até aqui mostra o contrário. **Recomendação: tratar a viabilidade como hipótese a ser testada, não como dado.**

---

## 4. MAPA DE EFICIÊNCIA — onde os espelhos concentraram votos (brechas para a Rosilene)

| Município | Ricardo Ayres | Filipe Martins | Eli Borges | Toinho Andrade |
|---|---:|---:|---:|---:|
| Palmas | 6.124 | **13.051** | **10.304** | 9.342 |
| Porto Nacional | 3.762 | 1.363 | 972 | 7.210 |
| Araguaína | — | 1.573 | 2.014 | — |
| Gurupi | 1.336 | 2.436 | 1.822 | 2.266 |
| Paraíso do TO | — | 1.239 | 1.457 | — |

- **Filipe e Eli são "capital-dependentes"** (Palmas concentra ~30–36% dos votos deles). Brecha = interior/médias cidades onde nenhum dos dois é forte.
- **Toinho e Ayres** têm voto mais distribuído (Porto Nacional, Miracema, Dianópolis, Lagoa da Confusão) — modelo capilar.
- Para a Rosilene, a base histórica é **Palmas + Guaraí** — exatamente onde Filipe/Eli são mais fortes (disputa direta no mesmo terreno). Brecha real estaria em cidades médias do interior ainda não dominadas por evangélicos.

---

## 5. FEFC 2026 — Republicanos (fonte: deep-research web, jun/2026)
- **Total nacional FEFC 2026:** R$ 4.961.519.777 (≈ R$ 4,96 bi), entre 30 partidos.
  Fonte: [TSE, jun/2026](https://www.tse.jus.br/comunicacao/noticias/2026/Junho/tse-divulga-distribuicao-do-fundo-especial-de-financiamento-de-campanha-para-as-eleicoes-2026) · [Gazeta do Povo](https://www.gazetadopovo.com.br/eleicoes/2026/veja-quanto-cada-partido-recebera-fundo-eleitoral-para-2026/)
- **Republicanos (10): R$ 348,6 milhões** — 7º maior (atrás de PL R$881,7M, PT R$615,4M, União R$526,2M, PSD R$421M, PP R$417,1M, MDB R$400M).
- **Recorte do diretório TO: NÃO ENCONTRADO** — o TSE não publica desagregação por estado; a distribuição interna é decidida pela executiva do partido (consultar diretório estadual diretamente).

---

## 6. Fábio Vaz — base municipal (prefeito de Palmeirópolis)
- **2016:** Fábio Vaz (PSD, nº 55) — **2.697 votos — ELEITO** prefeito de Palmeirópolis. (Todos os votos no município.)
- **2020:** não localizado no TSE como candidato a prefeito (provável fim do 2º mandato / impedimento de reeleição — coerente com "dois mandatos 2013–2020" reportado pela imprensa).
- **2012:** não coletado (layout antigo do TSE; pendente). — *Marcar "não encontrado" por ora.*
- **Dimensão da base real:** Palmeirópolis é cidade pequena; em 2022 Ricardo Ayres tirou 986 votos lá e Eli Borges 881. A base própria do Fábio (~2,7 mil em município pequeno) é modesta para uma federal, mas relevante como âncora regional no sul do estado.

---

## 7. PENDÊNCIAS — exigem coleta ao vivo nas plataformas (não verificáveis via dados abertos)

Os blocos abaixo **não passaram na verificação** do deep-research e precisam de raspagem direta (Instagram / Meta Ads Library). Posso fazer via navegador (Chrome) em seguida:

- [ ] **Redes sociais** (seguidores/engajamento/frequência): Ricardo Ayres, Rosilene Martins, Filipe Martins, Eli Borges, Coronel Barbosa, Fábio Vaz — comparar o **ativo orgânico** (onde a tese diz que a Rosilene lidera).
- [ ] **Meta Ad Library** (`facebook.com/ads/library`, filtro temas sociais/eleições, Brasil): quem dos pré-candidatos 2026 já roda tráfego pago e volume aproximado.
- [ ] **CEAP do Ricardo Ayres** (valor mensal exato): consultar `camara.leg.br/cota-parlamentar/` filtrando "Ricardo Ayres" / 2026.
- [ ] **Fábio Vaz 2012** (votos como prefeito): repositório legado do TSE.

### Já confirmado pelo deep-research (jun/2026):
- **Ricardo Ayres** — mandato ativo (57ª Leg., 2023–2027), **titular da CCJC**, suplente em Viação e Transportes; 163 proposições em 2026. [Câmara](https://www.camara.leg.br/deputados/220543)
- **Fábio Vaz** — ex-prefeito de Palmeirópolis (2 mandatos), saiu da Secretaria de Educação do TO em abr/2026, pré-candidato a federal pelo Republicanos.
- **Coronel (Márcio) Barbosa** — gravou vídeo com Flávio Bolsonaro, sinalizando alinhamento bolsonarista (possível ida ao PL de Eduardo Gomes).

---

## Apêndice — Arquivos desta pesquisa
- `extrair_gastos_tse.py` — script de coleta (reexecutável; usa cache em `cache_zips/`).
- `resultados_tse.json` — dados brutos estruturados (todas as rubricas, fontes de receita, top municípios).
- `RELATORIO-MESTRE.md` — este documento.
