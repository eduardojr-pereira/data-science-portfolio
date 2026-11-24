<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Análise da Demanda por Bicicletas Compartilhadas

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white&style=for-the-badge) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=for-the-badge)

*Análise histórica da demanda diária e horária, comportamento dos usuários, validação temporal e insights operacionais interativos.*

</div>

<p align="center">
  <a href="../../README.pt-BR.md#selected-projects">Voltar aos Projetos Selecionados</a> &nbsp;·&nbsp; <a href="../../README.pt-BR.md">Início do Portfólio</a> &nbsp;·&nbsp; <a href="https://eduardojr-pereira.github.io/data-science-portfolio/">Vitrine interativa</a>
</p>

<p align="center">
  <a href="https://eduardojr-pereira.github.io/data-science-portfolio/selected_projects/bike_sharing/reports/index.html"><strong>▶ Abrir relatório HTML interativo no navegador</strong></a>
</p>

---

## Nesta Página

<div align="center">

[Visão Geral](#overview) • [Contexto de Negócio](#business-context) • [Conteúdo](#contents) • [Tecnologias Utilizadas](#technologies) • [Instalação e Configuração](#installation) • [Testes e Validação](#validation)
[Instruções de Uso](#usage) • [Referências](#references) • [Licença](#license) • [Contato](#contact)

</div>

---

<a id="overview"></a>

## Visão Geral

**Problema de negócio:** Como a demanda por bicicletas varia ao longo do dia, do calendário e entre segmentos de usuários, e como esses padrões podem orientar decisões operacionais? O estudo analisa o Capital Bikeshare (Washington, D.C., 2011–2012) com **731 observações diárias e 17.379 registros horários** provenientes da mesma base UCI.

**Situação no portfólio:** Publicado como Projeto Selecionado no repositório GitHub, com relatório HTML interativo na vitrine. As bases diária e horária foram conciliadas, e uma versão anterior do notebook de 57 células foi executada sem erros. A reexecução integral do notebook após a mudança na geração do relatório ainda precisa ser verificada; a publicação não significa que essa reexecução ocorreu.

**Evidências dos modelos:** O modelo diário Polynomial ridge (degree 2) apresentou R² **-0.257** no teste cronológico, enquanto o modelo horário Random forest obteve R² **0.695**. Os erros RMSE/MAE têm unidades diferentes (aluguéis por dia versus por hora) e não podem ser comparados diretamente.

**Limite do estudo:** Os modelos utilizam informações meteorológicas observadas no mesmo dia ou na mesma hora. Trata-se de **estimação retrospectiva condicional da demanda**, não de previsão operacional validada nem de inferência causal. A reutilização de um período de teste já inspecionado limita as alegações de generalização independente.

**Knowledge Base:** [Machine Learning](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/05_machine_learning) · [Data Analysis & Visualization](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/02_data_analysis_visualization).

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="business-context"></a>

## Contexto de Negócio e Insights Operacionais

| Pergunta de negócio | Evidência e aplicação possível |
|---|---|
| Em qual horário a demanda se concentra? | O maior número médio de aluguéis por hora registrada ocorre entre **17:00 e 18:00**, com média de **461.5** aluguéis nas observações daquele horário. Isso pode orientar hipóteses sobre janelas de redistribuição, exigindo validação por estação. |
| Como a demanda mudou? | A média diária cresceu **64.4%** entre 2011 e 2012. Decisões de capacidade ancoradas só no primeiro ano podem subestimar volumes futuros; a comparação é descritiva, não causal. |
| Os segmentos de usuários se comportam igualmente? | As análises diária e horária distinguem usuários ocasionais e registrados. Os padrões por horário e dia útil ajudam a investigar necessidades associadas a deslocamento e lazer. |
| Os modelos podem ser usados em produção? | **Ainda não.** Diário: RMSE 2,101.4, MAE 1,968.9, R² -0.257. Horário: RMSE 121.8, MAE 84.9, R² 0.695. O clima observado no mesmo período e a reutilização do teste limitam essa aplicação. |

**Limitações para decisões:** A base não identifica estações individuais, rupturas de estoque, custos de redistribuição ou tempos de espera. Recomendações de escala e distribuição são hipóteses, não impactos comprovados. Horas sem registro não foram automaticamente imputadas como demanda zero.

<a id="contents"></a>

## Conteúdo

### Arquivos do Projeto

| Recurso | Finalidade |
|---|---|
| [Notebook](./bike_sharing_analysis.ipynb) | Notebook único das análises diária e horária |
| [Relatório HTML interativo](./reports/index.html) | Painel Plotly com gráficos diários e horários e ressalvas |
| [Dados diários](./datasets/day.csv) | Arquivo UCI original (731 dias) |
| [Dados horários](./datasets/hour.csv) | Arquivo UCI original (17.379 registros) |
| [Dependências](./requirements.txt) | Bibliotecas Python utilizadas |
| [Gerador do relatório](./build_bike_report.py) | Reconstrução do HTML a partir das exportações |
| [Métricas diárias](./outputs/metrics.json) | Resultados e metodologia diária |
| [Métricas horárias](./outputs/hourly/metrics.json) | Resultados e metodologia horária |
| [Comparação horária](./outputs/hourly/tables/hourly_model_comparison.csv) | Validação cruzada cronológica |
| [Comparação diária](./outputs/tables/model_comparison.csv) | Validação cruzada cronológica |

### Estrutura de Diretórios

```text
bike_sharing/
├── README.md / README.pt-BR.md
├── bike_sharing_analysis.ipynb
├── build_bike_report.py
├── requirements.txt
├── datasets/
│   ├── day.csv
│   └── hour.csv
├── outputs/
│   ├── metrics.json
│   ├── figures/ and tables/
│   └── hourly/
│       ├── metrics.json
│       ├── figures/
│       └── tables/
└── reports/
    └── index.html

```

Os dois arquivos UCI são usados e foram reconciliados. Checkpoints do Jupyter, backups locais e arquivos redundantes não devem ser publicados. O Plotly está incorporado ao relatório; a identidade visual externa pode precisar de conexão.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="technologies"></a>

## Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3 | Análise executável |
| pandas / NumPy | Validação dos dados e processamento numérico |
| scikit-learn | Validação temporal, pipelines e regressão |
| Matplotlib | Gráficos PNG reprodutíveis |
| Plotly | Visualizações interativas offline em HTML |
| JupyterLab | Execução e inspeção do notebook |

O projeto não depende de frameworks de aprendizado de máquina ou painéis externos desnecessários.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="installation"></a>

## Instalação e Configuração

Após copiar a pasta para `04_Projetos`, execute os comandos **dentro do diretório do projeto**:

```bash
python -m pip install -r requirements.txt
python -m pip check
jupyter lab
```

Você pode utilizar o ambiente `jupyter-env` já existente. Abra `bike_sharing_analysis.ipynb` e utilize **Restart Kernel → Run All Cells**. O notebook também consegue localizar seus arquivos quando executado a partir da raiz do repositório. A análise dispensa internet, embora a instalação das dependências possa exigir conexão.

A execução controlada foi realizada com **Python 3.13.5, pandas 2.2.3, scikit-learn 1.8.0, Matplotlib 3.10.8 e Plotly 6.5.2**. A compatibilidade com seu Python 3.14 local ainda precisa ser confirmada.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="validation"></a>

## Testes e Validação

| Verificação | Resultado registrado |
|---|---|
| Integridade dos dados | 731 registros diários + 17.379 horários (2011–2012); sem nulos ou duplicações data/hora; totais conciliados |
| Identidade da variável-alvo | `casual + registered = cnt` em todas as linhas |
| Hash do arquivo original | SHA-256 `a6bcf826782d3c0fbfdcbeead17cd0884185a0dafe8ff10cd48a874ee7ba18be` |
| Divisão treino/teste | 584 dias para desenvolvimento / 147 para teste cronológico |
| Seleção de modelos | `TimeSeriesSplit(n_splits=4)` em cada conjunto de desenvolvimento |
| Validação horária | 13.891 registros de treino; 3.488 de teste cronológico; Random Forest R² 0,695 |
| Pré-processamento | `Pipeline` com `ColumnTransformer` ajustado em cada fold |
| Melhor validação | **Polynomial ridge (degree 2)**, RMSE médio **1,431.31** |
| Teste final | RMSE **2,101.41**, MAE **1,968.90**, R² **-0.257** |
| Execução do notebook | Versão anterior: 57 células, 25 de código sem erros. Nova execução necessária após reordenar a geração do HTML |
| Relatório HTML | Gerado com base nos resultados exportados |
| Execução local | Concluída no `jupyter-env`; versão exata do Python a conferir separadamente |

**Ressalva entre versões:** O mesmo conjunto cronológico de teste já havia sido examinado no piloto v1. Embora a seleção de modelos nesta versão use apenas a validação no desenvolvimento, esse período não constitui mais um teste completamente inédito entre revisões. É necessária validação externa futura.

**Interpretação:** R² negativo no teste indica desempenho inferior à previsão constante igual à média do próprio período de teste. O resultado foi preservado sem ajustes orientados pelo mesmo conjunto de teste. Os números do notebook histórico não são comparáveis, pois o particionamento e o pré-processamento foram alterados.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="usage"></a>

## Instruções de Uso

1. Percorra o notebook único: EDA e modelos diários, padrões horários e avaliação independente dos modelos horários.
2. Consulte os CSVs gerados e `outputs/metrics.json` para verificar as métricas.
3. [Abra o relatório HTML interativo publicado](https://eduardojr-pereira.github.io/data-science-portfolio/selected_projects/bike_sharing/reports/index.html) no navegador, ou abra `reports/index.html` localmente. O visualizador de código do GitHub não executa o relatório como uma aplicação web.
4. Leia as limitações antes de divulgar métricas no portfólio ou currículo.

### Conclusões Práticas

A demanda média diária cresceu **64.4%** em 2012 e apresenta variação relevante ao longo do dia. Os dados permitem **investigar** janelas de operação, distribuição de oferta e diferenças entre segmentos, mas não medem a qualidade do serviço em cada estação.

O Random Forest horário (Random forest) alcançou R² **0.695** no teste histórico; o modelo diário atingiu **-0.257** e subestimou sistematicamente o final de 2012. Esses resultados não são previsões operacionais. Etapas futuras devem priorizar dados independentes, variáveis disponíveis no momento da previsão e validação prospectiva—sem otimizar repetidamente contra o mesmo teste.


<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="references"></a>

## Referências

| Recurso | Link |
|---|---|
| Dataset original e atribuição | [UCI Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) — Fanaee-T e Gama, DOI: 10.24432/C5W894 |
| Machine Learning | [Knowledge Base — Área 05](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/05_machine_learning) |
| Data Analysis & Visualization | [Knowledge Base — Área 02](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/02_data_analysis_visualization) |
| Preparação de Dados e Pipelines | [Guia Técnico](https://github.com/eduardojr-pereira/data-science-knowledge-base/blob/main/05_machine_learning/reference_materials/04_preparacao_pipelines.pdf) |
| Validação e Otimização | [Guia Técnico](https://github.com/eduardojr-pereira/data-science-knowledge-base/blob/main/05_machine_learning/reference_materials/11_validacao_otimizacao.pdf) |
| Regressão Linear | [Guia Técnico](https://github.com/eduardojr-pereira/data-science-knowledge-base/blob/main/05_machine_learning/reference_materials/12_regressao_linear.pdf) · [Cheat Sheet](https://github.com/eduardojr-pereira/data-science-knowledge-base/blob/main/05_machine_learning/cheat_sheets/cheat_sheet_regressao_linear.pdf) |
| Vazamento de dados e pipelines | [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) |
| Validação cronológica | [scikit-learn TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) |

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="license"></a>

## Licença

O **dataset** está atribuído a Fanaee-T e Gama pela UCI e atualmente é apresentado com licença **CC BY 4.0** ([detalhes da licença](https://creativecommons.org/licenses/by/4.0/)). A atribuição e o link de origem devem ser mantidos caso `day.csv` seja redistribuído.

O repositório `data-science-portfolio` **ainda não possui licença global definida para código e conteúdo**. As licenças MIT e CC BY-NC da Knowledge Base não são automaticamente aplicáveis a este projeto. A definição de licença para código e documentação depende de aprovação do proprietário. Bibliotecas, marcas e dados de terceiros mantêm seus próprios direitos.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="contact"></a>

<!-- EP-FOOTER:START -->
## Contato

<div align="center">

<a href="https://eduardo-pereira.webflow.io/" title="Site pessoal — Eduardo Junior Pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="Logo EP — Eduardo Junior Pereira" height="90"></a>

**Eduardo Junior Pereira**

*Economics · Data Science · Analytics*

<a href="mailto:eduardojr.pereira@gmail.com"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/gmail_icon.svg" alt="E-mail" height="27"></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/eduardo-jr-pereira/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/linkedin_icon.svg" alt="LinkedIn" height="27"></a>&nbsp;&nbsp;
<a href="https://github.com/eduardojr-pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/github_icon.svg" alt="GitHub" height="27"></a>

[Vamos nos conectar no LinkedIn para trocar ideias e oportunidades.](https://www.linkedin.com/in/eduardo-jr-pereira/)

[**Base de Conhecimento**](https://github.com/eduardojr-pereira/data-science-knowledge-base)

</div>

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---
<!-- EP-FOOTER:END -->
