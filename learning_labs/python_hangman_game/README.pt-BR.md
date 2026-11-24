<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Jogo da Forca — Laboratório de Python

![Python](https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/badges/technologies/python.svg) ![JavaScript](https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/badges/technologies/javascript.svg) ![HTML5](https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/badges/technologies/html5.svg) ![CSS](https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/badges/technologies/css.svg)

*Um jogo interativo de adivinhação de palavras desenvolvido para demonstrar fundamentos de programação em Python e no navegador.*

</div>

<p align="center">
  <a href="../../README.pt-BR.md#learning-labs">Voltar aos Learning Labs</a> &nbsp;·&nbsp; <a href="../../README.pt-BR.md">Início do Portfólio</a> &nbsp;·&nbsp; <a href="https://eduardojr-pereira.github.io/data-science-portfolio/">Vitrine interativa</a>
</p>

<p align="center">
  <a href="https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html"><strong>▶ Jogar Jogo da Forca no navegador</strong></a>
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
| [Jogar no navegador](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html) | Versão web interativa |
| [`hangman.py`](./hangman.py) | Implementação em Python para terminal |
| [`tests/test_hangman.py`](./tests/test_hangman.py) | Testes automatizados |
| [`web/report.js`](./web/report.js) | Lógica do jogo no navegador |
| [`web/report.css`](./web/report.css) | Layout e interações visuais |
| [`web/report.template.html`](./web/report.template.html) | Modelo-fonte da interface web |
| [`reports/index.html`](./reports/index.html) | Página web autônoma gerada |

## Tecnologias

Python 3 (biblioteca padrão, `unittest`) · HTML5 · CSS3 · JavaScript puro. Não é necessário instalar pacotes Python, Node.js, API externa ou backend para jogar.

## Instalação e Execução

Execute a partir da pasta do projeto:

```bash
python hangman.py
```

Ou utilize **[Jogar agora](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html)** para jogar no navegador sem instalar nada.

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

O código autoral está sujeito à [licença MIT](../../LICENSE-CODE.txt) e o conteúdo editorial e analítico autoral à [CC BY-NC 4.0](../../LICENSE-CONTENT.md), somente quando o autor detém os direitos necessários. Dados, bibliotecas, marcas e demais ativos de terceiros mantêm seus respectivos termos.

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
