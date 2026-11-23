"""Jogo da Forca: implementação didática em Python (biblioteca padrão)."""
from __future__ import annotations

import random
import unicodedata
from dataclasses import dataclass, field
from getpass import getpass

WORDS = ("FORMIGA", "BABUINO", "ENCEFALO", "ELEFANTE", "GIRAFA", "HAMBURGUER", "CHOCOLATE", "GIROSCOPIO")
DRAWINGS = (r"""
 +---+
 |   |
     |
     |
     |
     |
=========""", r"""
 +---+
 |   |
 O   |
     |
     |
     |
=========""", r"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========""", r"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========""", r"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========""", r"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========""", r"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========""")
MAX_ERRORS = len(DRAWINGS) - 1


def normalize_word(value: str) -> str:
    """Aceita letras com acento; remove acentos e espaços periféricos."""
    text = unicodedata.normalize("NFD", value.strip().upper())
    return "".join(ch for ch in text if unicodedata.category(ch) != "Mn")


def valid_word(value: str) -> bool:
    return bool(value) and value.isascii() and value.isalpha()


@dataclass
class Game:
    secret: str
    correct: set[str] = field(default_factory=set)
    incorrect: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.secret = normalize_word(self.secret)
        if not valid_word(self.secret):
            raise ValueError("A palavra precisa conter apenas letras (A-Z).")

    @property
    def won(self) -> bool:
        return set(self.secret) <= self.correct

    @property
    def lost(self) -> bool:
        return len(self.incorrect) >= MAX_ERRORS

    @property
    def finished(self) -> bool:
        return self.won or self.lost

    @property
    def masked(self) -> str:
        return " ".join(letter if letter in self.correct else "_" for letter in self.secret)

    def guess(self, text: str) -> str:
        if self.finished:
            return "A partida já terminou."
        letter = normalize_word(text)
        if len(letter) != 1 or not valid_word(letter):
            return "Digite uma única letra de A a Z."
        if letter in self.correct or letter in self.incorrect:
            return "Essa letra já foi utilizada."
        if letter in self.secret:
            self.correct.add(letter)
            return "Acertou!"
        self.incorrect.append(letter)
        return "Não há essa letra."


def choose_secret(mode: str, rng: random.Random | None = None, input_fn=input, secret_fn=getpass) -> str:
    if mode == "1":
        return (rng or random).choice(WORDS)
    while True:
        secret = normalize_word(secret_fn("Jogador 1, digite a palavra secreta (oculta): "))
        if valid_word(secret):
            return secret
        print("Use somente letras, sem espaços ou números.")


def run_game(input_fn=input, secret_fn=getpass, rng: random.Random | None = None) -> None:
    print("\n=== JOGO DA FORCA ===")
    while True:
        mode = input_fn("Modo: [1] Um jogador  [2] Dois jogadores: ").strip()
        if mode in ("1", "2"):
            break
        print("Escolha 1 ou 2.")
    while True:
        game = Game(choose_secret(mode, rng=rng, input_fn=input_fn, secret_fn=secret_fn))
        while not game.finished:
            print(DRAWINGS[len(game.incorrect)])
            print("Palavra:", game.masked)
            print("Erros:", ", ".join(game.incorrect) or "nenhum", f"({len(game.incorrect)}/{MAX_ERRORS})")
            message = game.guess(input_fn("Sua letra: "))
            print(message)
        print(DRAWINGS[len(game.incorrect)])
        print("Palavra:", game.masked)
        print(f"{'Você venceu!' if game.won else 'Fim de jogo!'} A palavra era {game.secret}.")
        if input_fn("Jogar novamente? [s/N]: ").strip().lower() not in ("s", "sim"):
            print("Até a próxima!")
            return


if __name__ == "__main__":
    run_game()
