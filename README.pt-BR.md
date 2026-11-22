<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Portfólio de Ciência de Dados

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white&style=for-the-badge) ![Data Science](https://img.shields.io/badge/Data-Science-21618C?style=for-the-badge)

*Uma coleção bilíngue de projetos aplicados selecionados, experimentos de aprendizado e exercícios acadêmicos autorais em Ciência de Dados.*

</div>

---

## Nesta Página

<div align="center">

[Visão Geral](#overview) • [Conteúdo](#contents) • [Instalação e Configuração](#setup) • [Instruções de Uso](#usage)

[Testes e Validação](#validation) • [Referências](#references) • [Licença](#license) • [Contato](#contact)

</div>

---

<a id="overview"></a>

## Visão Geral

Este repositório reúne trabalhos práticos e complementa a [Base de Conhecimento em Ciência de Dados](https://github.com/eduardojr-pereira/data-science-knowledge-base). Ele separa projetos aplicados selecionados de exercícios de aprendizagem, facilitando a navegação conforme a finalidade e a maturidade de cada trabalho.

**Situação atual:** Bike Sharing foi promovido localmente a primeiro Projeto Selecionado. Os dados diário e horário foram conciliados, o notebook único anterior, com 57 células, foi executado (nova validação após a migração pendente) e o relatório interativo segue em revisão final. A publicação do novo caminho está pendente; os modelos são análises retrospectivas, não preditores de produção.

**Idiomas:** esta apresentação está disponível em inglês e português brasileiro. Os futuros projetos poderão utilizar qualquer um dos idiomas; seus READMEs indicarão o conteúdo efetivamente disponível.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="contents"></a>

## Conteúdo

### Coleções de Projetos

| Coleção | Finalidade |
|---|---|
| [Projetos Selecionados](./selected_projects/README.pt-BR.md) | Projetos curados com problema de negócio, resultados, limitações e execução reproduzível |
| [Learning Labs](./learning_labs/README.pt-BR.md) | Notebooks menores e estudos técnicos, independentemente da origem acadêmica |
| [Experimentos Independentes](./learning_labs/independent_experiments/README.pt-BR.md) | Investigações exploratórias ainda não promovidas a estudos de caso selecionados |

### Primeiro Projeto Selecionado

| Projeto | Relatório Interativo (após publicação) | Notebook |
|---|---|---|
| Bike Sharing — Demanda e Insights Operacionais | [GitHub Pages](https://eduardojr-pereira.github.io/data-science-portfolio/selected_projects/bike_sharing/reports/) | [Abrir notebook](./selected_projects/bike_sharing/bike_sharing_analysis.ipynb) |

### Navegação por Tema

Regressão, classificação, NLP e análise de demanda serão categorias da vitrine, não pastas vazias. Novos projetos serão indexados após validação.

### Organização de Diretórios

~~~text
data-science-portfolio/
├── README.md / README.pt-BR.md
├── selected_projects/
│   ├── README.md / README.pt-BR.md
│   └── bike_sharing/
│       ├── bike_sharing_analysis.ipynb
│       ├── report_builder.py
│       ├── datasets/ (day.csv, hour.csv)
│       ├── outputs/ (diário e horário)
│       └── reports/index.html
└── learning_labs/
    ├── README.md / README.pt-BR.md
    └── independent_experiments/
~~~

Bike Sharing é o primeiro Projeto Selecionado promovido localmente. Os materiais históricos continuam preservados fora do portfólio; novos estudos serão incorporados aos Learning Labs após revisão.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="setup"></a>

## Instalação e Configuração

**1. Clone o repositório:**

~~~bash
git clone https://github.com/eduardojr-pereira/data-science-portfolio.git
cd data-science-portfolio
~~~

**2. Consulte as coleções disponíveis:**

~~~bash
ls selected_projects
ls learning_labs
ls learning_labs/independent_experiments
~~~

Não existe **`requirements.txt` global**. O piloto Bike Sharing possui dependências e instruções próprias. Consulte o README de cada projeto para verificar ambiente, acesso aos dados e comandos de execução. Não pressuponha que todos os futuros projetos utilizem o mesmo ambiente Python.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="usage"></a>

## Instruções de Uso

Comece por **Projetos Selecionados** para conhecer análises aplicadas, resolução de problemas e conclusões. Consulte **Laboratórios de Aprendizado** para experimentos menores e exercícios acadêmicos autorais que demonstram técnicas específicas.

Antes da publicação, cada trabalho candidato será revisado quanto à autoria, proveniência e direitos de redistribuição dos dados, informações sensíveis, reprodutibilidade, integridade dos outputs e documentação. Materiais didáticos de terceiros não serão apresentados como trabalhos autorais. Os acervos históricos originais permanecerão preservados separadamente.

Os futuros projetos deverão documentar objetivo, fontes de dados, preparação do ambiente, métodos, resultados, limitações e licenças aplicáveis.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="validation"></a>

## Testes e Validação

| Verificação | Situação documentada |
|---|---|
| Estrutura de diretórios e placeholders | Publicada |
| Apresentação bilíngue | Disponível |
| Projetos selecionados | Bike Sharing promovido localmente; publicação pendente |
| Learning labs | Área reservada para futuros estudos |
| Execução e reprodutibilidade dos projetos | Validação e limitações do Bike Sharing documentadas no README específico |

**A publicação do piloto não valida os próximos projetos.** Cada README específico documentará a execução, a reprodutibilidade e as limitações metodológicas efetivamente verificadas.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="references"></a>

## Referências

| Recurso | Link |
|---|---|
| Base de Conhecimento em Ciência de Dados | [Notebooks de estudo e referências técnicas](https://github.com/eduardojr-pereira/data-science-knowledge-base) |
| Identidade Visual EP | [Logotipo e ícones compartilhados](https://github.com/eduardojr-pereira/ep-brand-assets) |
| JupyterLab | [Documentação oficial](https://jupyterlab.readthedocs.io/en/stable/) |
| Python | [Documentação oficial](https://docs.python.org/3/) |

As referências específicas de cada projeto serão documentadas junto ao respectivo trabalho.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="license"></a>

## Licença

**Ainda não foi definida uma licença geral** para este repositório. Antes de publicar os projetos, revisaremos os direitos sobre códigos originais, documentação e dados de terceiros e registraremos as licenças aplicáveis. As licenças da Base de Conhecimento, que é um repositório separado, não se aplicam automaticamente a este portfólio.

Datasets externos, imagens, bibliotecas e recursos de identidade visual mantêm seus próprios direitos e condições de uso.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="contact"></a>

## Contato

<div align="center">

<a href="https://eduardo-pereira.webflow.io/" title="Personal website — Eduardo Junior Pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="EP logo — Eduardo Junior Pereira" height="90"></a>

**Eduardo Junior Pereira**

*Economics • Data Science • Python*

<a href="mailto:eduardojr.pereira@gmail.com"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/gmail_icon.svg" alt="Email" height="27"></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/eduardo-jr-pereira/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/linkedin_icon.svg" alt="LinkedIn" height="27"></a>&nbsp;&nbsp;
<a href="https://github.com/eduardojr-pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/github_icon.svg" alt="GitHub" height="27"></a>

[Vamos nos conectar no LinkedIn para trocar ideias e oportunidades.](https://www.linkedin.com/in/eduardo-jr-pereira/)

[**Base de Conhecimento**](https://github.com/eduardojr-pereira/data-science-knowledge-base) &nbsp;•&nbsp; [**Site Pessoal**](https://eduardo-pereira.webflow.io/)

</div>

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---
