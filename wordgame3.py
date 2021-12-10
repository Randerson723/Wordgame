import random


class Word:

    def __init__(self):
        words = ("programmer", "rhubarb", "oriented", "algorithm",
                 "engineer", "dictionary", "monotonic", "funcionality", "horizontal", "vertical")
        self._word = random.choice(words)
        self.letters_in_word = set(self._word)

    def word(self):
        return self._word

    def progress(self, guesses):
        progress_string = ""
        for char in self.word:
            if guesses.guessed(char):
                progress_string = progress_string + "" + char + ""
            else:
                progress_string = progress_string + "_"
        return(progress_string)

    def guessed(self, guesses):
        letters_guessed = self.letters_in_word.intersection(
            guesses.guesses_made)
        if letters_guessed == self.letters_in_word:
            return ("\n You are correct!!")
        else:
            return ("\n You are incorrect!!")


class Guesses:
    def __init__(self):
        self.guesses_made = set()

    def guessed(self, char):
        if char in self.guesses_made:
            return ("\n You are correct!!")
        else:
            return ("\n You are incorrect!!")

    def count(self, guess, word):
        self.guesses_made.add(guess)

    def guesses_made(self):
        guesses_list = list(self.guesses_made)
        guesses_list.sort()
        guesses_string = ""
    
    



class Game:
    print("#"*25)
    print("Welcome to Wordgame")
    print("#"*25)

    def get_letter(self, guesses):
        while True:
            char = input("\nEnter your guess: ")
                if 
