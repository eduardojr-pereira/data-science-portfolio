<a id="readme-top"></a>

<div align="center">

| [English](./README.md) · [Português](./README.pt-BR.md) |

# Portfólio de Ciência de Dados

*Economia, Ciência de Dados e Analytics aplicados a problemas de negócio.*

</div>

<p align="center"><a href="https://eduardojr-pereira.github.io/data-science-portfolio/"><strong>Explorar o portfólio interativo</strong></a></p>

<div align="center">

[Visão Geral](#overview) · [Projetos](#projects) · [Estrutura de Diretórios](#directory-structure)<br>
[Repositórios Relacionados](#related-repositories) · [Licença](#license) · [Contato](#contact)

</div>

---

<a id="overview"></a>

## Visão Geral

Este portfólio reúne projetos de Ciência de Dados e Analytics que conectam minha formação em Ciências Econômicas (UFV) e pós-graduação em Ciência de Dados (PUC) à resolução de problemas práticos. É o complemento aplicado da Base de Conhecimento em Ciência de Dados.

Os projetos são organizados conforme sua finalidade e maturidade. A documentação e as experiências interativas dos dois projetos atuais estão disponíveis em inglês e português brasileiro. Cada projeto documenta suas dependências, metodologia, validação e limitações; não há um ambiente Python único para todo o repositório. Novos trabalhos são revisados quanto à autoria, procedência e direitos dos dados, informações sensíveis, reprodutibilidade e documentação antes da inclusão.


---

<a id="projects"></a>

## Projetos

Explore o portfólio por meio de três coleções de projetos, organizadas conforme sua finalidade, profundidade técnica e maturidade.

- [**Projetos Selecionados**](#selected-projects) — Estudos de caso aplicados a problemas reais de negócio e análise de dados.
- [**Laboratórios de Aprendizado**](#learning-labs) — Projetos práticos voltados ao desenvolvimento de competências técnicas e à implementação de soluções.
- [**Experimentos Independentes**](#independent-experiments) — Investigações exploratórias e abordagens experimentais.

<a id="selected-projects"></a>

### Projetos Selecionados

| Projeto | Área e tecnologias | Recursos |
|---|---|---|
| **Bike Sharing — Demanda e Insights Operacionais** | Análise de demanda · Regressão e avaliação de modelos · Python, pandas, scikit-learn, Plotly | [Documentação](./selected_projects/bike_sharing/README.pt-BR.md) · [Código-fonte](./selected_projects/bike_sharing/) · [Demonstração online](https://eduardojr-pereira.github.io/data-science-portfolio/selected_projects/bike_sharing/reports/) |

O estudo analisa padrões históricos de demanda diária e horária, segmentos de usuários e avaliação temporal de modelos.

> [!CAUTION]
> Os resultados são retrospectivos, não previsões validadas para uso em produção. As limitações de reexecução do notebook estão documentadas no README do projeto.

<a id="learning-labs"></a>

### Laboratórios de Aprendizado

| Projeto | Área e tecnologias | Recursos |
|---|---|---|
| **Hangman Game — Jogo da Forca** | Fundamentos de programação · Python, JavaScript, HTML, CSS | [Documentação](./learning_labs/python_hangman_game/README.pt-BR.md) · [Código-fonte](./learning_labs/python_hangman_game/) · [Demonstração online](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html) |

Jogo de adivinhação de palavras com versões no terminal e no navegador, modos de um e dois jogadores e interface bilíngue no navegador.

<a id="independent-experiments"></a>

### Experimentos Independentes

Nenhum experimento foi publicado nesta coleção até o momento.

<p align="right"><sub><a href="#readme-top">↑ Voltar ao topo</a></sub></p>

---

<a id="directory-structure"></a>

## Estrutura de Diretórios

<details>
<summary><strong>Árvore do repositório</strong></summary>

```text
data-science-portfolio/
├── .github/
│   └── workflows/
├── .gitignore
├── LICENSE-CODE.txt
├── LICENSE-CONTENT.md
├── README.md
├── README.pt-BR.md
├── config/
│   └── projects.json
├── independent_experiments/
│   └── .gitkeep
├── learning_labs/
│   └── python_hangman_game/
├── selected_projects/
│   └── bike_sharing/
└── tools/
    └── ep_brand.py
```

</details>

Cada projeto possui documentação e estrutura próprias.

- `config/` — Contém o catálogo de projetos.
- `tools/` — Contém o adaptador de integração com a fonte canônica EP Brand.

<p align="right"><sub><a href="#readme-top">↑ Voltar ao topo</a></sub></p>

---

<a id="related-repositories"></a>

## Repositórios Relacionados

| Repositório | Finalidade |
|---|---|
| [Data Science Knowledge Base](https://github.com/eduardojr-pereira/data-science-knowledge-base) | Notebooks de estudo, guias e materiais de referência técnica |
| [EP Brand Assets](https://github.com/eduardojr-pereira/ep-brand-assets) | Identidade visual, componentes compartilhados e infraestrutura de apresentação |

<p align="right"><sub><a href="#readme-top">↑ Voltar ao topo</a></sub></p>

---

<a id="license"></a>

## Licença

Estas licenças se aplicam somente aos materiais sobre os quais o autor detém os direitos necessários; código e conteúdo editorial podem estar sujeitos a licenças distintas.

<table>
<tr>
<td align="center" valign="middle"><a href="./LICENSE-CODE.txt"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/badges/licenses/mit.svg" alt="MIT"></a></td>
<td valign="middle"><strong>Código-fonte</strong> | Scripts autorais, código dos notebooks, testes e implementação dos relatórios.</td>
</tr>
<tr>
<td align="center" valign="middle"><a href="./LICENSE-CONTENT.md"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/badges/licenses/cc_by_nc_4_0.svg" alt="CC BY-NC 4.0"></a></td>
<td valign="middle"><strong>Conteúdo editorial e analítico</strong> | READMEs, explicações, estudos de caso, narrativas dos relatórios e conteúdo visual autoral.</td>
</tr>
<tr>
<td align="center" valign="middle">Termos de terceiros</td>
<td valign="middle"><strong>Conteúdo externo</strong> | Datasets, imagens, marcas e outros recursos; aplicam-se os respectivos termos de uso.</td>
</tr>
</table>

> [!WARNING]
> Dados de terceiros, bibliotecas e componentes do EP Brand mantêm seus respectivos termos de licença. Verifique a procedência, os direitos de redistribuição e os avisos aplicáveis antes de publicar novos projetos ou dados.

<p align="right"><sub><a href="#readme-top">↑ Voltar ao topo</a></sub></p>

---

<a id="contact"></a>

<!-- EP-FOOTER:START -->
## Contato

<div align="center">

<a href="https://eduardo-pereira.webflow.io/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="Logo EP" height="90"></a>

Vamos nos conectar e trocar ideias e oportunidades.

<a href="mailto:eduardojr.pereira@gmail.com"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/gmail_icon.svg" alt="E-mail" height="27"></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/eduardo-jr-pereira/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/linkedin_icon.svg" alt="LinkedIn" height="27"></a>&nbsp;&nbsp;
<a href="https://github.com/eduardojr-pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/github_icon.svg" alt="GitHub" height="27"></a>&nbsp;&nbsp;
<a href="https://discord.com/users/533043855122235393"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/discord_icon.svg" alt="Discord" height="27"></a>

</div>

<!-- EP-FOOTER:END -->
