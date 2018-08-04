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
    def __init__(self, word):
        self.answer = word
        self.masked = '*' * len(word)
        
        if self.answer == '':
            raise InvalidWordException
        
    def perform_attempt(self, guess):
        if len(guess) > 1:
            raise InvalidGuessedLetterException
        
        if guess in self.answer:
            new_string = ''
            for index,char in enumerate(self.answer):
                if char.lower() == guess.lower():
                    new_string += char
                else:
                    new_string += self.masked[index]
            self.masked = new_string    
            return GuessAttempt(guess, hit=True)
        
"""
for i in range(len(self.answer):
    masked_char = self.masked[i]
    answer_char = self.answer[i]
    if answer_char.lower() == guess.lower():
        new_string += answer_char
    else:
        new_string += masked_char
self.masked = new_string

for answer_char, masked_char in zip(self.answer, self.masked):
    
    if answer_char.lower() == guess.lower():
        new_string += answer_char
    else:
        new_string += masked_char
self.masked = new_string
"""

class HangmanGame(object):
    pass
