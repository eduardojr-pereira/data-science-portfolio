# Hangman Game — Python Learning Lab

[Português](README.pt-BR.md) · [Interactive web demo](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python/jogo_da_forca/reports/index.html)

An interactive Hangman game in **Python** and **HTML/CSS/JavaScript** for practicing programming fundamentals. This is an educational mini-project, not a machine-learning or data-analytics model.

## Features

- Two game modes: single-player random word and two-player secret word.
- Browser demo with bilingual interface (Portuguese/English), on-screen and physical keyboard, responsive design, accessible status messages and EP footer.
- CLI game using only Python standard library; accent normalization, input validation, repeated-guess handling and six mistakes maximum.
- Eight automated `unittest` tests.

## Play online

Open the [interactive Hangman game](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python/jogo_da_forca/reports/index.html) after the GitHub Pages deployment.

## Run with Python

```bash
python forca.py
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## File structure

| Path | Purpose |
|---|---|
| `forca.py` | CLI game and game state |
| `tests/test_forca.py` | Unit tests |
| `web/game.template.html` | Source template for web game |
| `web/game.css` | Web styles and motion |
| `web/game.js` | Browser game logic |
| `web/ep_footer_motion.css` | EP footer animation override |
| `reports/index.html` | Standalone generated demo published by Pages |
| `README.pt-BR.md` | Portuguese documentation |

## Technical notes

The Python and browser versions intentionally implement equivalent rules in separate runtimes; the browser version does not execute Python. It does not send words or guesses to a server. In two-player mode, the first player should enter the secret privately. Avoid using sensitive phrases as secret words. Browser code does not require npm, CDNs or a back end.

The source notebook is archived separately, not shipped with this package. The shared EP footer is injected from the portfolio's `vendor/ep-brand-assets` assets by `tools/integrar_jogo_da_forca.py`.

## Validation

The Python test suite reported **8 passing tests** in the author's Linux environment on 22 November 2026. Browser interaction and responsive rendering should be checked locally before committing.
