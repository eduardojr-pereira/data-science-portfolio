<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Hangman Game — Python Learning Lab

![Python](https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/badges/technologies/python.svg) ![JavaScript](https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/badges/technologies/javascript.svg) ![HTML5](https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/badges/technologies/html5.svg) ![CSS](https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/badges/technologies/css.svg)

*An interactive word-guessing game built to demonstrate programming fundamentals in Python and the browser.*

</div>

<p align="center">
  <a href="../../README.md#learning-labs">Back to Learning Labs</a> &nbsp;·&nbsp; <a href="../../README.md">Portfolio home</a> &nbsp;·&nbsp; <a href="https://eduardojr-pereira.github.io/data-science-portfolio/">Interactive showcase</a>
</p>

<p align="center">
  <a href="https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html"><strong>▶ Play the interactive game in your browser</strong></a>
</p>

---

## Overview

Hangman is an educational **Learning Lab**, not a machine-learning or data-analytics project. This repository includes the command-line Python implementation. The previously published browser version uses HTML, CSS and JavaScript. The two versions follow equivalent game rules, but the browser does **not** execute the Python source. Migration of the web version to the canonical EP Brand architecture is pending.

## Features

| Feature | Description |
|---|---|
| Single-player mode | A random word is selected for the player to guess |
| Two-player mode | One player enters the secret word; the other guesses |
| Guess handling | Letters are validated; repeated guesses do not consume attempts |
| Game progress | Progressive hangman drawing, up to six incorrect guesses, win/loss detection |
| Web interface (previous published version) | Responsive layout, on-screen and physical keyboard, English/Portuguese language selection |
| Privacy | Guessing happens locally, without sending the secret word to a server |

## Contents

| Resource | Purpose |
|---|---|
| [Play online](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html) | Interactive browser version |
| [`hangman.py`](./hangman.py) | Python command-line implementation |
| [`tests/test_hangman.py`](./tests/test_hangman.py) | Automated unit tests |

## Technologies

Python 3 (standard library, `unittest`) for the terminal implementation. The previously published web version uses HTML5, CSS3 and vanilla JavaScript. No Python packages, Node.js installation, external API or backend are required to play either existing version.

## Setup and Installation

Run from this project's directory:

```bash
python hangman.py
```

Alternatively, use **[Play online](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html)** to play in the browser without installing anything.

## Testing and Validation

```bash
python -m unittest discover -s tests -v
```

**Verified on 22 November 2026:** all **8 automated Python tests passed** in the local Linux environment. Manual terminal playthroughs also covered a single-player loss, a two-player win, repeated letters and invalid guesses. The browser layout and navigation were reviewed and approved locally; this is not a claim of exhaustive browser compatibility testing.

## How to Use

Choose one-player or two-player mode, then guess letters before reaching six mistakes. In two-player mode, the first player should enter the word privately. On the web, use the on-screen keyboard or the physical keyboard and select your preferred language. Use the replay control to start a new round.

The initial Jupyter notebook was kept outside this published project package by decision of the author. This checkpoint maintains the Python source and tests; the linked web demonstration belongs to the previous published version.

## References

This is an original learning exercise based on the traditional Hangman word game. For related theoretical material, see the [Python Programming Knowledge Base](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/01_python_programming).

## License

Original code is subject to the [MIT License](../../LICENSE-CODE.txt) and original editorial and analytical content to [CC BY-NC 4.0](../../LICENSE-CONTENT.md), only where the author holds the necessary rights. Third-party data, libraries, trademarks and other assets retain their respective terms.

---

<a id="contact"></a>

<!-- EP-FOOTER:START -->
## Contact

<div align="center">

<a href="https://eduardo-pereira.webflow.io/" title="Personal website — Eduardo Junior Pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="EP logo — Eduardo Junior Pereira" height="90"></a>

**Eduardo Junior Pereira**

*Economics · Data Science · Analytics*

<a href="mailto:eduardojr.pereira@gmail.com"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/gmail_icon.svg" alt="Email" height="27"></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/eduardo-jr-pereira/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/linkedin_icon.svg" alt="LinkedIn" height="27"></a>&nbsp;&nbsp;
<a href="https://github.com/eduardojr-pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/github_icon.svg" alt="GitHub" height="27"></a>

[Let's connect on LinkedIn to exchange ideas and opportunities.](https://www.linkedin.com/in/eduardo-jr-pereira/)

[**Knowledge Base**](https://github.com/eduardojr-pereira/data-science-knowledge-base)

</div>

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---
<!-- EP-FOOTER:END -->
