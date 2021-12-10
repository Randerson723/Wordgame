import random

class Word:
    
    word = ["Russell", "Python", "Intergrated", "Contextual"]
    
    
    def _in_it_(self, guesses, word):
        self.guesses= guesses
        self.word= word
        word = random.choice(word).lower()
        print(word)
        

    def word_in_progress(self, word, guess):
        word_in_progress = ""
        for letter in word:
            if letter in guess:
              word_in_progress += letter
        else:
            word_in_progress += "*"
        return word_in_progress


def instructions():

    print("Welcome to Wordgame, you will have  chances to discover the word:")
    print("###" * 25)










def main():
    
    

    lettersguessed = []
    Done = False

    while not done:
        instructions()
        
        while True:
            guess = input("What letter do you think is in the word:")
            word = Word._in_it_

    



        


        
