from .exceptions import *


class GuessAttempt(object):
    def __init__(self, letter, hit=None, miss=None):
        self.letter = letter
        self.hit = hit
        self.miss = miss
        
        if hit and miss:
            raise InvalidGuessAttempt
        
    def is_hit(self):
        if self.hit:
            return True
        return False
        
    def is_miss(self):
        if self.miss:
            return True
        return False


class GuessWord(object):
    pass


class HangmanGame(object):
    pass
