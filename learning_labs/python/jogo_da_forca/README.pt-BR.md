# Jogo da Forca — Laboratório de Python

[English](README.md) · [Jogar no navegador](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python/jogo_da_forca/reports/index.html)

Jogo da Forca interativo em **Python** e **HTML/CSS/JavaScript** para demonstrar fundamentos de programação. É um miniprojeto didático, não um modelo de aprendizado de máquina ou análise de dados.

## Funcionalidades

- Modo individual com sorteio de palavras e modo para duas pessoas com palavra secreta.
- Demonstração web em português/inglês com teclado virtual e físico, layout responsivo, mensagens acessíveis e rodapé EP.
- Versão de terminal feita somente com a biblioteca padrão do Python: normalização de acentos, validação de entradas, controle de palpites repetidos e seis erros máximos.
- Oito testes automatizados com `unittest`.

## Jogar no navegador

Abra o [jogo interativo](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python/jogo_da_forca/reports/index.html) após a publicação do GitHub Pages.

## Executar em Python

```bash
python forca.py
```

## Testar

```bash
python -m unittest discover -s tests -v
```

## Estrutura

| Arquivo | Função |
|---|---|
| `forca.py` | Jogo e estado da partida no terminal |
| `tests/test_forca.py` | Testes unitários |
| `web/game.template.html` | Modelo-fonte da página web |
| `web/game.css` | Estilos e animações |
| `web/game.js` | Lógica do jogo no navegador |
| `web/ep_footer_motion.css` | Ajustes de animação do rodapé EP |
| `reports/index.html` | Página autônoma gerada para o GitHub Pages |
| `README.md` | Documentação em inglês |

## Observações técnicas

As versões Python e JavaScript implementam regras equivalentes em ambientes diferentes; o navegador não executa Python. Não há servidor ou transmissão de palavras e palpites. No modo para duas pessoas, o primeiro jogador deve digitar a palavra sem que o segundo veja. Evite usar informações sensíveis como palavras secretas. A interface web não exige npm, CDN ou backend.

O notebook original permanece arquivado separadamente, fora deste pacote. O rodapé EP é gerado a partir do componente compartilhado em `vendor/ep-brand-assets` pelo script `tools/integrar_jogo_da_forca.py`.

## Validação

A suíte Python apresentou **8 testes aprovados** no Linux do autor em 22/11/2026. A interação web e a responsividade ainda precisam de conferência visual local antes do commit.
