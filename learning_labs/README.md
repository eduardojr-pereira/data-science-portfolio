<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Learning Labs

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black&style=for-the-badge) ![Learning Labs](https://img.shields.io/badge/Learning-Labs-21618C?style=for-the-badge)

*Hands-on programming and data-science experiments with documented scope and validation.*

</div>

<p align="center">
  <a href="../README.md">Portfolio home</a> &nbsp;·&nbsp; <a href="../selected_projects/README.md">Selected Projects</a> &nbsp;·&nbsp; <a href="https://eduardojr-pereira.github.io/data-science-portfolio/">Interactive showcase</a>
</p>

<p align="center">
  <a href="https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html"><strong>▶ Play Hangman in your browser</strong></a>
</p>

---

## On This Page

<div align="center">

[Overview](#overview) • [Published Labs](#labs) • [Technologies](#technologies) • [Getting Started](#setup) • [Testing and Validation](#validation) • [Organization](#organization) • [References](#references) • [License](#license) • [Contact](#contact)

</div>

---

<a id="overview"></a>

## Overview

This collection contains smaller, focused projects for learning programming concepts, testing and experimentation. **Learning Labs** are distinct from **Selected Projects**, which present larger applied case studies and analyses.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="labs"></a>

## Published Labs

| Lab | Area | Resources |
|---|---|---|
| **Hangman Game** | Python · JavaScript · Programming Fundamentals | [Documentation](./python_hangman_game/README.md) · [Play online](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html) · [Python](./python_hangman_game/forca.py) · [Tests](./python_hangman_game/tests/test_forca.py) |

**Hangman Game** — Word-guessing game with terminal and browser editions, single-player and two-player modes, PT-BR/EN interface and eight automated Python tests.

[Explore the interactive showcase](https://eduardojr-pereira.github.io/data-science-portfolio/)

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="technologies"></a>

## Technologies

| Technology | Use |
|---|---|
| Python 3 | CLI game logic and `unittest` tests |
| HTML, CSS, JavaScript | Browser game interface without a back end |

Dependencies and commands are documented per lab; this collection does not define a shared Python environment.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="setup"></a>

## Getting Started

You can play directly in the browser: [Play now](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html).

To run the Python version locally:

```bash
git clone https://github.com/eduardojr-pereira/data-science-portfolio.git
cd data-science-portfolio/learning_labs/python_hangman_game
python forca.py
```

No third-party Python packages are required to run the CLI game.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="validation"></a>

## Testing and Validation

On 22 November 2026, the Hangman Python suite passed **8 out of 8 tests** on the author’s Linux machine. This confirms the cases covered by the suite, not automated browser-interface testing.

```bash
python -m unittest discover -s tests -v
```

Run this command inside `learning_labs/python_hangman_game/`. Additional labs will document their own validation independently.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="organization"></a>

## Organization

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

[Independent Experiments](../independent_experiments/README.md) — reserved category with no individual projects published at this review.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="references"></a>

## References

| Resource | Link |
|---|---|
| Data Science Knowledge Base | [GitHub](https://github.com/eduardojr-pereira/data-science-knowledge-base) |
| Portfolio home | [Main README](../README.md) |
| Hangman Game | [Technical documentation](./python_hangman_game/README.md) |

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="license"></a>

## License

The `data-science-portfolio` repository currently does not declare a repository-wide license for original code and documentation. Third-party libraries, datasets and assets retain their respective terms.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

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
