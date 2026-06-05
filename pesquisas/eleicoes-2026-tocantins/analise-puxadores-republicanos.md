# Os Puxadores do Republicanos-TO — critérios, votos e investimento

**Análise para a estratégia de Rosilene Martins · Deputado Federal 2026**

> **Data:** 05/06/2026 · Complementa o `dossie-estrategico-rosilene-martins.md`.
> **Sobre os números:** os **valores exatos de gasto por candidato estão no DivulgaCandContas/Dados Abertos do TSE**, que este ambiente não acessa (egress bloqueado — 403). Os números **confirmados** abaixo vêm de fontes públicas/imprensa. Para o **gasto digital exato por candidato**, use o script anexo `extrair_gastos_tse.py` (roda na sua máquina). O que é estimativa está marcado como tal.

---

## 1. Que critério define um "puxador"? (a pergunta central)

A constatação mais importante — e que corrige a premissa: **para 3 dos 4 puxadores, "puxador" NÃO vem de votação passada.** Eles nunca disputaram deputado federal. O critério real é **capital político institucional**, não histórico de urna.

| Puxador | Critério que o coloca nessa posição | Já foi candidato a Fed.? | Votos federais comprovados |
|---|---|---|---|
| **Ricardo Ayres** | **Incumbência** — mandato federal em curso, maior relator da história do TO; visibilidade legislativa. | ✅ 2022 | **45.880** (5º do estado) |
| **Coronel Márcio Barbosa** | **Base corporativa + pauta** — ex-comandante-geral da PM, segurança pública, padrinhos nacionais (Tarcísio, Bolsonaro). | ❌ Nunca | — (estreante) |
| **Atos Gomes** | **Máquina estatal** — ex-secretário de Esportes; capilaridade do governo e proximidade com Wanderlei. | ❌ Nunca | — (estreante) |
| **Fábio Vaz** | **Máquina estatal + base municipal** — ex-secretário de Educação; **ex-prefeito de Palmeirópolis (2013–2020)** e ex-vereador; rede de professores. | ❌ Nunca (a Fed.) | — (tem voto municipal, não federal) |

➡️ **Tradução:** o que faz deles "puxadores" é **estrutura pronta** (mandato, governo do estado, corporação, prefeitura), que entrega votos sem precisar construí-los do zero. **Apenas o Ayres tem voto federal testado.** Para os outros três, qualquer projeção de votação 2026 é **aposta**, não retrospecto. Isso é decisivo para a Rosilene: **ela não está atrás de gente com "fama de urna" — está atrás de gente com máquina.** A disputa real é por *estrutura*, não por popularidade.

*Fontes: [Câmara — eleitos TO 2022](https://www.camara.leg.br/noticias/911284-republicanos-elege-3-dos-8-deputados-do-tocantins-pp-e-pl-2/); [Gazeta do Cerrado — Coronel Márcio Barbosa](https://gazetadocerrado.com.br/politica/coronel-marcio-barbosa-recebe-apoios-no-sudeste-e-amplia-articulacoes-rumo-a-camara-federal/); [Agência Tocantins — Fábio Vaz deixa Seduc](https://www.agenciatocantins.com.br/noticia/106535/fabio-vaz-deixa-seduc-para-disputar-vaga-na-camara-federal-e-promete-defender-avancos-da-educacao/).*

---

## 2. Votos e investimento — o que é número REAL

### 2.1 Benchmark confirmado (TO, deputado federal, 2022)
| Indicador | Valor | Confiança |
|---|---|---|
| Custo médio por voto no TO | **R$ 37,56** (2º mais caro do Brasil) | confirmado (Metrópoles) |
| Gasto médio por eleito | **~R$ 1,6 milhão** | confirmado |
| Teto legal de gasto (2022) | **R$ 3.176.572,53** | confirmado (TSE) |
| Teto legal de gasto (2026) | **~R$ 3,85 milhões** | confirmado (TSE) |
| Pior eficiência entre eleitos | **Lázaro Botelho — R$ 170,70/voto** (gastou caro p/ 13.168 votos) | confirmado |

### 2.2 Ranking de votos dos 8 eleitos (2022)
| # | Eleito | Partido | Votos |
|---|---|---|---|
| 1 | Toinho Andrade | Republicanos | 63.813 |
| 2 | Vicentinho Júnior | PP | 55.292 |
| 3 | Alexandre Guimarães | Republicanos | 54.703 |
| 4 | Carlos Gaguim | União Brasil | 52.203 |
| 5 | **Ricardo Ayres** | **Republicanos** | **45.880** |
| 6 | Filipe Martins | PL | 36.293 |
| 7 | Eli Borges | PL | 35.171 |
| 8 | Lázaro Botelho | PP | 13.668 |

### 2.3 O que NÃO foi possível confirmar aqui (e por quê)
Os **valores individuais de arrecadação, gasto total e gasto digital** de cada candidato **não foram publicados pela imprensa** — existem apenas no sistema do TSE, que este ambiente não alcança. Aplicando o benchmark ao Ayres (45.880 votos × ~R$37,56) chega-se a uma **ordem de grandeza de ~R$ 1,7 milhão** de gasto — mas isso é **estimativa derivada**, não o número declarado. O valor exato (e a fatia digital) sai do script da seção 4.

---

## 3. Gasto com digital / tráfego — como obter o número real

A imprensa não detalha isso, mas o TSE classifica cada despesa por categoria. As rubricas "digitais" na prestação de contas são:
- **Impulsionamento de conteúdos** (tráfego pago — o que você chama de "tráfego");
- **Criação/inclusão de páginas na internet e redes sociais**;
- **Produção de conteúdo / material para internet**.

> **Referência de mercado (não é dado do TO):** campanhas proporcionais costumam declarar entre **~8% e ~20%** do orçamento em rubricas digitais/internet. O número **exato por candidato** sai do `extrair_gastos_tse.py`.

**Por que isso importa para a Rosilene:** este é provavelmente o **único terreno onde ela já larga na frente** dos puxadores. Ayres é parlamentar (comunicação institucional), o Coronel tem base offline, Atos e Fábio são máquina de governo — **nenhum deles tem ativo digital orgânico relevante.** A Rosilene tem **~66 mil seguidores reais e uma marca de palco**. Digital é a assimetria a explorar.

---

## 4. O script para fechar os números exatos (anexo)

`pesquisas/eleicoes-2026-tocantins/extrair_gastos_tse.py` — rode na sua máquina (rede com acesso ao TSE):

```bash
python extrair_gastos_tse.py --ano 2022 --uf TO --cargo "DEPUTADO FEDERAL"
```

Ele baixa os Dados Abertos do TSE e devolve, **por candidato**: gasto total, **gasto digital (impulsionamento/internet/redes)** e o **% digital**, mais o ranking. É assim que você obtém o número real do Ricardo Ayres (e de qualquer outro) — incluindo a parte de tráfego — que a imprensa não publica. (O `src/mcp_brasil/data/tse/client.py` do próprio repo complementa com `total_votos` e fundo via API DivulgaCandContas.)

---

## 5. Como a Rosilene poderia se igualar

Premissa realista: **ela não se iguala aos puxadores no terreno deles** (não tem mandato, máquina de governo nem corporação). A igualdade possível é por **dinheiro + vantagem digital + disciplina territorial**. Os números:

### Meta de votos para "jogar no nível dos puxadores"
- Faixa dos eleitos médios: **35–45 mil votos**.
- Ela parte de **~5 mil** (melhor resultado). O salto é de **7–9x**.

### Quanto custaria igualar (estimativas de trabalho)
| Objetivo | Votos-alvo | Investimento estimado | Observação |
|---|---|---|---|
| Igualar o **piso de eleição** (faixa 6º–7º) | ~35 mil | **R$ 2,0–2,8 mi** | candidato sem máquina paga acima da média R$37,56/voto |
| Igualar o **Ricardo Ayres** (5º) | ~45 mil | **R$ 2,8–3,5 mi** | perto do teto de R$ 3,85 mi |

> Por que mais caro que a média? Porque os puxadores têm **votos "subsidiados"** por estrutura gratuita (mandato, governo, corporação, igreja). A Rosilene precisa **comprar** o que eles ganham de graça — logo, o custo por voto dela tende a ser maior. É o mesmo motivo pelo qual o Lázaro pagou R$170/voto.

### Onde investir para reduzir essa desvantagem (a fatia digital)
Como o digital é a assimetria dela, a recomendação é **superalocar** essa rubrica em relação aos concorrentes:
- **Digital/tráfego: 25–30% do orçamento** (vs. ~10–15% de uma campanha tradicional). Converter os 66 mil seguidores em base georreferenciada por cidade, com tráfego segmentado no público evangélico/feminino das cidades-alvo (Palmas, central-norte, circuito gospel).
- **Eventos/shows: 15–18%** — o show gospel é "mídia paga barata" que os puxadores não conseguem replicar.
- **Lideranças/cabos: 28–30%** — para suprir a ausência de máquina institucional.

➡️ **Síntese tática:** igualar os puxadores em volume bruto de votos exige **R$ 2–3,5 mi** — patamar de alto risco para quem nunca passou de 5 mil votos. O caminho inteligente **não é "igualar", é flanquear**: dominar o digital (onde eles são fracos) e o circuito gospel (que é só dela), mirando primeiro a **vaga por sobra da legenda** (Cenário 1 do dossiê, R$ 500–900 mil) e só escalar para o nível dos puxadores se a base própria responder até agosto.

---

## 6. Resumo

1. **Puxador aqui = estrutura, não fama de urna.** Só o Ayres tem voto federal testado (45.880); os outros 3 são estreantes com máquina (governo/PM/prefeitura).
2. **Números de gasto individual não são públicos via imprensa** — só no TSE. Benchmark real: R$37,56/voto, ~R$1,6 mi por eleito, teto 2026 R$3,85 mi.
3. **Gasto digital exato → script anexo** (`extrair_gastos_tse.py`).
4. **Igualar os puxadores custaria R$ 2–3,5 mi** e é aposta de alto risco; o movimento esperto é **flanquear pelo digital + gospel** e disputar a sobra, não competir de igual para igual na estrutura.
5. **A vantagem da Rosilene é digital** — terreno onde os 4 puxadores são fracos. É onde o investimento dela rende mais por real gasto.

---

### Pendências para fechar com número fino (rodar o script)
- [ ] Gasto total e **% digital** de Ricardo Ayres (2022) — `extrair_gastos_tse.py`.
- [ ] Mesmo dado para Filipe Martins e Eli Borges (evangélicos eleitos) — comparáveis ao perfil dela.
- [ ] Fatia digital média dos eleitos do TO — para calibrar o orçamento da seção 5.
- [ ] Votação municipal de Fábio Vaz (Palmeirópolis) — dimensiona a base prévia dele.
