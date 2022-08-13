import random


class Die:
    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    def roll(self):
        new_score = random.randint(1, 6)
        self._score = new_score
        return new_score
