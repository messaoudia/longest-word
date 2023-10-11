import random
import string

class Game:
    """
    Game class
    """
    def __init__(self) -> None:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for i in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        return all([letter in self.grid for letter in word.upper()])
