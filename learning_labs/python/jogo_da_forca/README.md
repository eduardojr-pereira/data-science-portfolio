<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Hangman Game — Python Learning Lab

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black&style=for-the-badge) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white&style=for-the-badge)

*An interactive word-guessing game built to demonstrate programming fundamentals in Python and the browser.*

</div>

<p align="center">
  <a href="../../README.md">Back to Learning Labs</a> &nbsp;·&nbsp; <a href="../../../README.md">Portfolio home</a> &nbsp;·&nbsp; <a href="https://eduardojr-pereira.github.io/data-science-portfolio/">Interactive showcase</a>
</p>

<p align="center">
  <a href="https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python/jogo_da_forca/reports/index.html"><strong>▶ Play the interactive game in your browser</strong></a>
</p>

---

## Overview

Hangman is an educational **Learning Lab**, not a machine-learning or data-analytics project. It has two implementations: a command-line game in Python and a browser-based game in HTML, CSS and JavaScript. The two versions follow equivalent game rules, but the browser does **not** execute the Python source.

## Features

| Feature | Description |
|---|---|
| Single-player mode | A random word is selected for the player to guess |
| Two-player mode | One player enters the secret word; the other guesses |
| Guess handling | Letters are validated; repeated guesses do not consume attempts |
| Game progress | Progressive hangman drawing, up to six incorrect guesses, win/loss detection |
| Web interface | Responsive layout, on-screen and physical keyboard, English/Portuguese language selection |
| Privacy | Guessing happens locally, without sending the secret word to a server |

## Contents

| Resource | Purpose |
|---|---|
| [Play online](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python/jogo_da_forca/reports/index.html) | Interactive browser version |
| [`forca.py`](./forca.py) | Python command-line implementation |
| [`tests/test_forca.py`](./tests/test_forca.py) | Automated unit tests |
| [`web/game.js`](./web/game.js) | Browser game logic |
| [`web/game.css`](./web/game.css) | Web layout and interactions |
| [`web/game.template.html`](./web/game.template.html) | Source template for the web interface |
| [`web/ep_footer_motion.css`](./web/ep_footer_motion.css) | Shared EP footer motion styling |
| [`reports/index.html`](./reports/index.html) | Generated standalone web page |

## Technologies

Python 3 (standard library, `unittest`) · HTML5 · CSS3 · JavaScript (vanilla). No Python packages, Node.js installation, external API or backend are required to play.

## Setup and Installation

Run from this project's directory:

```bash
python forca.py
```

Alternatively, use **[Play online](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python/jogo_da_forca/reports/index.html)** to play in the browser without installing anything.

## Testing and Validation

```bash
python -m unittest discover -s tests -v
```

**Verified on 22 November 2026:** all **8 automated Python tests passed** in the local Linux environment. Manual terminal playthroughs also covered a single-player loss, a two-player win, repeated letters and invalid guesses. The browser layout and navigation were reviewed and approved locally; this is not a claim of exhaustive browser compatibility testing.

## How to Use

Choose one-player or two-player mode, then guess letters before reaching six mistakes. In two-player mode, the first player should enter the word privately. On the web, use the on-screen keyboard or the physical keyboard and select your preferred language. Use the replay control to start a new round.

The initial Jupyter notebook was kept outside this published project package by decision of the author; the maintained version is the Python source plus the web demonstration.

## References

This is an original learning exercise based on the traditional Hangman word game. For related theoretical material, see the [Python Programming Knowledge Base](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/01_python_programming).

## License

The `data-science-portfolio` repository has **no declared repository-wide license** for its original code or documentation at the time of this review. Do not assume that another repository's license applies. Third-party icons and brand assets retain their respective terms.

---

<a id="contact"></a>

## Contact

<div align="center">

<a href="https://eduardo-pereira.webflow.io/" title="Personal website — Eduardo Junior Pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="EP logo — Eduardo Junior Pereira" height="90"></a>

**Eduardo Junior Pereira**

*Economics • Data Science • Python*

<a href="mailto:eduardojr.pereira@gmail.com"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/gmail_icon.svg" alt="Email" height="27"></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/eduardo-jr-pereira/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/linkedin_icon.svg" alt="LinkedIn" height="27"></a>&nbsp;&nbsp;
<a href="https://github.com/eduardojr-pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/github_icon.svg" alt="GitHub" height="27"></a>

[Let's connect on LinkedIn to exchange ideas and opportunities.](https://www.linkedin.com/in/eduardo-jr-pereira/)

[**Knowledge Base**](https://github.com/eduardojr-pereira/data-science-knowledge-base) &nbsp;•&nbsp; [**Personal Website**](https://eduardo-pereira.webflow.io/)

</div>

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---
