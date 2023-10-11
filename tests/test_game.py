from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        g = Game()
        # exercise
        grid = g.grid
        # verify
        assert type(grid) is list
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_letters

    def test_is_valid(self):
        # setup
        g = Game()
        grid_str = "TO"

        # exercise
        g.grid = list(grid_str)

        # verify
        assert g.is_valid("toto")
        assert not g.is_valid("titi")

        # teardown
        assert g.grid == list(grid_str)

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        g = Game()
        g.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert g.is_valid('FEUN') is False
