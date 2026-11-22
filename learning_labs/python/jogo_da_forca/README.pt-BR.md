<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Jogo da Forca — Laboratório de Python

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black&style=for-the-badge) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white&style=for-the-badge)

*Um jogo interativo de adivinhação de palavras desenvolvido para demonstrar fundamentos de programação em Python e no navegador.*

</div>

<p align="center">
  <a href="../../README.pt-BR.md">Voltar aos Learning Labs</a> &nbsp;·&nbsp; <a href="../../../README.pt-BR.md">Início do Portfólio</a> &nbsp;·&nbsp; <a href="https://eduardojr-pereira.github.io/data-science-portfolio/">Vitrine interativa</a>
</p>

<p align="center">
  <a href="https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python/jogo_da_forca/reports/index.html"><strong>▶ Jogar Jogo da Forca no navegador</strong></a>
</p>

---

## Visão Geral

O Jogo da Forca é um **Learning Lab** educacional, não um projeto de aprendizado de máquina ou análise de dados. Há duas implementações: um jogo de terminal em Python e uma versão para navegador em HTML, CSS e JavaScript. As regras são equivalentes, mas o navegador **não executa o código Python**.

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| Um jogador | Uma palavra aleatória é escolhida para adivinhação |
| Dois jogadores | Uma pessoa informa a palavra secreta e a outra tenta descobri-la |
| Validação | Letras são verificadas; tentativas repetidas não consomem chances |
| Evolução da partida | Desenho progressivo, até seis erros, identificação de vitória e derrota |
| Interface web | Layout responsivo, teclado virtual e físico, alternância português/inglês |
| Privacidade | Os palpites são processados localmente, sem envio da palavra a um servidor |

## Conteúdo

| Recurso | Finalidade |
|---|---|
| [Jogar no navegador](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python/jogo_da_forca/reports/index.html) | Versão web interativa |
| [`forca.py`](./forca.py) | Implementação em Python para terminal |
| [`tests/test_forca.py`](./tests/test_forca.py) | Testes automatizados |
| [`web/game.js`](./web/game.js) | Lógica do jogo no navegador |
| [`web/game.css`](./web/game.css) | Layout e interações visuais |
| [`web/game.template.html`](./web/game.template.html) | Modelo-fonte da interface web |
| [`web/ep_footer_motion.css`](./web/ep_footer_motion.css) | Animações do rodapé EP |
| [`reports/index.html`](./reports/index.html) | Página web autônoma gerada |

## Tecnologias

Python 3 (biblioteca padrão, `unittest`) · HTML5 · CSS3 · JavaScript puro. Não é necessário instalar pacotes Python, Node.js, API externa ou backend para jogar.

## Instalação e Execução

Execute a partir da pasta do projeto:

```bash
python forca.py
```

Ou utilize **[Jogar agora](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python/jogo_da_forca/reports/index.html)** para jogar no navegador sem instalar nada.

## Testes e Validação

```bash
python -m unittest discover -s tests -v
```

**Verificado em 22/11/2026:** os **8 testes automatizados de Python passaram** no ambiente Linux local. Também foram testadas manualmente uma derrota no modo individual, uma vitória com dois jogadores, letras repetidas e entradas inválidas. O layout e a navegação da versão web foram revisados e aprovados localmente; isso não equivale a um teste exaustivo de compatibilidade entre navegadores.

## Como Usar

Escolha o modo individual ou para duas pessoas e descubra a palavra antes de cometer seis erros. No modo para duas pessoas, o primeiro jogador deve informar a palavra sem que o outro veja. Na versão web, use o teclado virtual ou físico e selecione o idioma preferido. O controle de nova partida reinicia o jogo.

O notebook Jupyter original foi preservado fora do pacote publicado por decisão do autor; a versão mantida neste projeto é o código Python com a demonstração web.

## Referências

Este é um exercício autoral baseado no tradicional Jogo da Forca. Para material teórico relacionado, consulte a [Base de Conhecimento — Programação em Python](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/01_python_programming).

## Licença

O repositório `data-science-portfolio` **não possui licença geral declarada** para seus códigos e documentação autorais até esta revisão. Não se deve presumir que a licença de outro repositório se aplique. Ícones e recursos de identidade visual de terceiros mantêm suas condições específicas.

---

<a id="contact"></a>

## Contato

<div align="center">

<a href="https://eduardo-pereira.webflow.io/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="Logo EP — Eduardo Junior Pereira" height="90"></a>

**Eduardo Junior Pereira**
*Economia • Ciência de Dados • Python*

<a href="mailto:eduardojr.pereira@gmail.com"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/gmail_icon.svg" alt="Email" height="27"></a>&nbsp;&nbsp;<a href="https://www.linkedin.com/in/eduardo-jr-pereira/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/linkedin_icon.svg" alt="LinkedIn" height="27"></a>&nbsp;&nbsp;<a href="https://github.com/eduardojr-pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/github_icon.svg" alt="GitHub" height="27"></a>

[Vamos nos conectar no LinkedIn para trocar ideias e oportunidades.](https://www.linkedin.com/in/eduardo-jr-pereira/)

[**Base de Conhecimento**](https://github.com/eduardojr-pereira/data-science-knowledge-base) &nbsp;•&nbsp; [**Portfólio no GitHub**](https://github.com/eduardojr-pereira/data-science-portfolio) &nbsp;•&nbsp; [**Site Pessoal**](https://eduardo-pereira.webflow.io/)

</div>

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>
