import random
import string
import requests

class Game:
    """
    Game class
    """
    def __init__(self) -> None:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for i in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        word = word.upper()
        is_grid_valid = all([letter in self.grid for letter in word])
        return is_grid_valid & self._check_dictionnary(word)

    def _check_dictionnary(self, word:str):
        request = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        return request.json()["found"]
