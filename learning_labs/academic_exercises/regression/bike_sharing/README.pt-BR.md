<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Análise da Demanda por Bicicletas Compartilhadas

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white&style=for-the-badge) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=for-the-badge)

*Análise de demanda diária, comparação de regressões sem vazamento de dados e relatório HTML interativo.*

</div>

---

## Nesta Página

<div align="center">

[Visão Geral](#overview) • [Conteúdo](#contents) • [Tecnologias Utilizadas](#technologies) • [Instalação e Configuração](#installation) • [Testes e Validação](#validation)  
[Instruções de Uso](#usage) • [Referências](#references) • [Licença](#license) • [Contato](#contact)

</div>

---

<a id="overview"></a>

## Visão Geral

Este exercício acadêmico de regressão analisa a contagem diária de aluguéis do sistema Capital Bikeshare, em Washington, D.C., entre **2011 e 2012**. A análise combina exploração ampliada dos dados e comparação cronológica de sete modelos de referência/regressão, além de uma demonstração separada de otimização restrita ao treinamento, evitando divisões aleatórias e ajustando o pré-processamento dentro dos conjuntos de treinamento.

**Escopo importante:** as entradas incluem medições do clima observadas **no mesmo dia** dos aluguéis. Portanto, trata-se de *estimação condicional da demanda*, e **não** de previsão operacional para o dia seguinte. As associações observadas não demonstram causalidade.

**Situação:** **piloto em revisão — publicação ainda não aprovada.** O notebook revisado e o relatório foram executados em ambiente de validação independente, e você já executou a versão piloto v1 localmente sem erros. A versão ampliada v2 ainda aguarda teste local. O notebook histórico original permanece preservado.

**Resultado relevante:** Polynomial ridge (degree 2) foi selecionado pela validação temporal realizada apenas no treinamento, mas a avaliação final apresentou **R² = -0.257**, indicando generalização insatisfatória.

**Knowledge Base:** [Machine Learning](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/05_machine_learning) · [Data Analysis & Visualization](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/02_data_analysis_visualization).

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="contents"></a>

## Conteúdo

### Arquivos do Projeto

| Recurso | Finalidade |
|---|---|
| [Notebook](./bike_sharing_analysis.ipynb) | Análise de regressão documentada e executada |
| [Relatório HTML interativo](./reports/index.html) | Gráficos offline, métricas verificadas e limitações |
| [Dataset](./datasets/day.csv) | Base diária UCI original (731 dias) |
| [Dependências](./requirements.txt) | Intervalos de versões testados |
| [Gerador do relatório](./report_builder.py) | Reconstrói o HTML a partir dos resultados validados |
| [Comparação dos modelos](./outputs/tables/model_comparison.csv) | Escores de validação cruzada temporal |
| [Previsões de teste](./outputs/tables/holdout_predictions.csv) | Estimativas no conjunto cronológico final |
| [Métricas estruturadas](./outputs/metrics.json) | Fonte única das métricas do relatório |
| [Figuras](./outputs/figures/) | Dez gráficos PNG reprodutíveis |
| [Importância de variáveis](./outputs/tables/random_forest_feature_importance.csv) | Importância obtida exclusivamente com dados de treinamento |

### Estrutura de Diretórios

```text
bike_sharing/
├── README.md
├── README.pt-BR.md
├── requirements.txt
├── bike_sharing_analysis.ipynb
├── report_builder.py
├── datasets/
│   └── day.csv
├── outputs/
│   ├── metrics.json
│   ├── figures/
│   │   ├── correlation_matrix.png
│   │   ├── cross_validation_comparison.png
│   │   ├── demand_patterns.png
│   │   ├── distributions.png
│   │   ├── holdout_predictions.png
│   │   ├── random_forest_importances.png
│   │   ├── random_forest_tree_excerpt.png
│   │   ├── rentals_by_weather.png
│   │   ├── rider_type_mix.png
│   │   └── weekday_and_season.png
│   └── tables/
│       ├── model_comparison.csv
│       ├── holdout_predictions.csv
│       └── random_forest_feature_importance.csv
└── reports/
    └── index.html
```

O checkpoint, o ZIP redundante e o arquivo horário `hour.csv` não foram copiados porque não participam desta análise. O HTML contém o JavaScript de gráficos para uso offline; a logo EP vinculada externamente ainda precisa de conexão para ser exibida.

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
| Integridade do dataset | 731 registros diários; 01/01/2011 a 31/12/2012; sem dados ausentes |
| Identidade da variável-alvo | `casual + registered = cnt` em todas as linhas |
| Hash do arquivo original | SHA-256 `a6bcf826782d3c0fbfdcbeead17cd0884185a0dafe8ff10cd48a874ee7ba18be` |
| Divisão treino/teste | 584 dias para desenvolvimento / 147 para teste cronológico |
| Seleção de modelos | `TimeSeriesSplit(n_splits=4)` apenas no desenvolvimento |
| Pré-processamento | `Pipeline` com `ColumnTransformer` ajustado em cada fold |
| Melhor validação | **Polynomial ridge (degree 2)**, RMSE médio **1,431.31** |
| Teste final | RMSE **2,101.41**, MAE **1,968.90**, R² **-0.257** |
| Execução do notebook | 43 células concluídas sem erros no ambiente de teste |
| Relatório HTML | Gerado com base nos resultados exportados |
| Validação local da v2 no Python 3.14 | Pendente (piloto v1 já executado localmente) |

**Ressalva entre versões:** O mesmo conjunto cronológico de teste já havia sido examinado no piloto v1. Embora a seleção de modelos nesta versão use apenas a validação no desenvolvimento, esse período não constitui mais um teste completamente inédito entre revisões. É necessária validação externa futura.

**Interpretação:** R² negativo no teste indica desempenho inferior à previsão constante igual à média do próprio período de teste. O resultado foi preservado sem ajustes orientados pelo mesmo conjunto de teste. Os números do notebook histórico não são comparáveis, pois o particionamento e o pré-processamento foram alterados.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="usage"></a>

## Instruções de Uso

1. Percorra o notebook para compreender dicionário de dados, validação, segmentação dos usuários, análises climáticas e sazonais, correlações, modelos de regressão, otimização, importância das variáveis e avaliação final.
2. Consulte os CSVs gerados e `outputs/metrics.json` para verificar as métricas.
3. Abra `reports/index.html` no navegador para visualizar o relatório executivo. O visualizador de arquivos do GitHub não é um hospedador de páginas HTML; o GitHub Pages será configurado somente após aprovação.
4. Leia as limitações antes de divulgar métricas no portfólio ou currículo.

### Conclusões Práticas

Os aluguéis anuais registrados passaram de 1.243.103 em 2011 para 2.049.576 em 2012. Essa diferença é descritiva, não causal. O modelo selecionado não generalizou bem para o teste no final de 2012. Uma próxima iteração científica deve investigar a disponibilidade das variáveis, mudanças temporais de distribuição e um protocolo de avaliação independente, em vez de otimizar repetidamente contra o mesmo teste.

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

## Contato

<div align="center">

<a href="https://eduardo-pereira.webflow.io/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="EP logo — Eduardo Junior Pereira" height="90"></a>

**Eduardo Junior Pereira**  
*Economics • Data Science • Python*

<a href="mailto:eduardojr.pereira@gmail.com"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/gmail_icon.svg" alt="Email" height="27"></a>&nbsp;&nbsp;<a href="https://www.linkedin.com/in/eduardo-jr-pereira/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/linkedin_icon.svg" alt="LinkedIn" height="27"></a>&nbsp;&nbsp;<a href="https://github.com/eduardojr-pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/github_icon.svg" alt="GitHub" height="27"></a>

[Conecte-se comigo no LinkedIn para trocar ideias e oportunidades.](https://www.linkedin.com/in/eduardo-jr-pereira/)

[**Knowledge Base**](https://github.com/eduardojr-pereira/data-science-knowledge-base) &nbsp;•&nbsp; [**GitHub Portfolio**](https://github.com/eduardojr-pereira/data-science-portfolio) &nbsp;•&nbsp; [**Personal Website**](https://eduardo-pereira.webflow.io/)

</div>

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

