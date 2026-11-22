<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Learning Labs

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black&style=for-the-badge) ![Learning Labs](https://img.shields.io/badge/Learning-Labs-21618C?style=for-the-badge)

*Laboratórios práticos e experimentos autorais de programação e Ciência de Dados.*

</div>

<p align="center">
  <a href="../README.pt-BR.md">Início do Portfólio</a> &nbsp;·&nbsp; <a href="../selected_projects/README.pt-BR.md">Projetos Selecionados</a> &nbsp;·&nbsp; <a href="https://eduardojr-pereira.github.io/data-science-portfolio/">Vitrine interativa</a>
</p>

<p align="center">
  <a href="https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html"><strong>▶ Jogar Jogo da Forca no navegador</strong></a>
</p>

---

## Nesta Página

<div align="center">

[Visão Geral](#overview) • [Laboratórios Publicados](#labs) • [Tecnologias](#technologies) • [Como Executar](#setup) • [Testes e Validação](#validation) • [Organização](#organization) • [Referências](#references) • [Licença](#license) • [Contato](#contact)

</div>

---

<a id="overview"></a>

## Visão Geral

Esta coleção reúne projetos práticos de escopo reduzido, com foco em conceitos de programação, testes e experimentação. Os **Learning Labs** são separados dos **Projetos Selecionados**, que apresentam estudos de caso aplicados e análises mais abrangentes.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="labs"></a>

## Laboratórios Publicados

| Laboratório | Área | Recursos |
|---|---|---|
| **Jogo da Forca** | Python · JavaScript · Fundamentos de programação | [Documentação](./python_hangman_game/README.pt-BR.md) · [Jogar online](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html) · [Python](./python_hangman_game/forca.py) · [Testes](./python_hangman_game/tests/test_forca.py) |

**Jogo da Forca** — Jogo de adivinhação com versão no terminal e no navegador, modos individual e duas pessoas, interface PT-BR/EN e oito testes automatizados em Python.

[Explorar a vitrine interativa](https://eduardojr-pereira.github.io/data-science-portfolio/)

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="technologies"></a>

## Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python 3 | Lógica do jogo no terminal e testes com `unittest` |
| HTML, CSS, JavaScript | Interface do jogo executada no navegador, sem backend |

As dependências e os comandos devem ser consultados no README de cada laboratório; esta coleção não define um ambiente Python compartilhado.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="setup"></a>

## Como Executar

O jogo pode ser acessado diretamente no navegador: [Jogar agora](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html).

Para executar a versão Python localmente:

```bash
git clone https://github.com/eduardojr-pereira/data-science-portfolio.git
cd data-science-portfolio/learning_labs/python_hangman_game
python forca.py
```

Não é necessário instalar bibliotecas externas para executar o jogo Python.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="validation"></a>

## Testes e Validação

Em 22/11/2026, a suíte Python do Jogo da Forca passou em **8 de 8 testes** na máquina Linux do autor. Isso valida os casos cobertos pela suíte, mas não substitui testes automatizados de interface no navegador.

```bash
python -m unittest discover -s tests -v
```

Execute o comando dentro de `learning_labs/python_hangman_game/`. Novos laboratórios terão sua validação documentada individualmente.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="organization"></a>

## Organização

```text
learning_labs/
├── README.md
├── README.pt-BR.md
└── python_hangman_game/
    ├── README.md / README.pt-BR.md
    ├── forca.py
    ├── tests/
    ├── web/
    └── reports/index.html
```

[Experimentos Independentes](../independent_experiments/README.pt-BR.md) — categoria reservada, sem projetos individuais publicados até esta revisão.

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="references"></a>

## Referências

| Recurso | Link |
|---|---|
| Base de Conhecimento | [GitHub](https://github.com/eduardojr-pereira/data-science-knowledge-base) |
| Portfólio principal | [README principal](../README.pt-BR.md) |
| Jogo da Forca | [Documentação técnica](./python_hangman_game/README.pt-BR.md) |

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---

<a id="license"></a>

## Licença

O repositório `data-science-portfolio` não declara atualmente uma licença global para código e documentação autorais. Bibliotecas, dados e recursos de terceiros mantêm suas próprias condições de uso.

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
