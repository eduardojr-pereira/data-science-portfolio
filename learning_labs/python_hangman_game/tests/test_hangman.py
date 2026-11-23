"""Testes determinísticos, sem interação nem execução automática ao importar."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hangman import Game, MAX_ERRORS, WORDS, choose_secret, normalize_word, valid_word


class GameTests(unittest.TestCase):
    def test_normalize_and_validate(self):
        self.assertEqual(normalize_word("  maçã "), "MACA")
        self.assertTrue(valid_word("MACA"))
        for text in ("", "AB C", "ABC3", "ABC-"):
            self.assertFalse(valid_word(text))

    def test_win_repeated_letters(self):
        game = Game("BABA")
        self.assertEqual(game.guess("b"), "Acertou!")
        self.assertEqual(game.masked, "B _ B _")
        self.assertEqual(game.guess("a"), "Acertou!")
        self.assertTrue(game.won)
        self.assertFalse(game.lost)

    def test_repeated_guess_does_not_count_error(self):
        game = Game("GATO")
        game.guess("z")
        self.assertEqual(game.guess("z"), "Essa letra já foi utilizada.")
        self.assertEqual(len(game.incorrect), 1)

    def test_invalid_guess_does_not_count(self):
        game = Game("GATO")
        for guess in ("12", "", "AB", "@"): self.assertEqual(game.guess(guess), "Digite uma única letra de A a Z.")
        self.assertEqual(game.incorrect, [])

    def test_loses_at_limit(self):
        game = Game("A")
        for letter in "BCDEFG":
            game.guess(letter)
        self.assertEqual(len(game.incorrect), MAX_ERRORS)
        self.assertTrue(game.lost)
        self.assertEqual(game.guess("a"), "A partida já terminou.")

    def test_bad_secret(self):
        with self.assertRaises(ValueError): Game("duas palavras")

    def test_words_are_valid(self):
        self.assertTrue(all(valid_word(word) for word in WORDS))

    def test_choose_secret_with_rng(self):
        class Stub:
            def choice(self, words): return words[0]
        self.assertEqual(choose_secret("1", rng=Stub()), WORDS[0])

if __name__ == "__main__":
    unittest.main()
