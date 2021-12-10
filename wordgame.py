import random 

def choose_word():
    words = ["Russell", "Python", "Intergrated","Contextual"]
    word = random.choice(words).lower()
    return word

def word_in_progress(word, guess):
    word_in_progress = ""
    for letter in word:
        if letter in guess:
            word_in_progress += letter
        else:
            word_in_progress += "*"
    return word_in_progress
    



def main(word):
    lettersguessed = []
    chances = int(len(word) * 1.5)
    print("You are looking for a word that is  " + str(len(word)) + "letters long.")

    while True:
        if chances != 0:
            print("\nYou have " + str(chances) + " chances left.")
            print("Word so far: " + word_in_progress(word, lettersguessed))
            print("Letters guessed: " + str(lettersguessed))
            guess = input("Guess: ").lower()[0]
           
            if word_in_progress(word, lettersguessed) == word:
                print("\nCongratulations! You got it correct:" + word)
                break
            else:
                chances -= 1
                if guess in word:
                    print("Correct letter!")
                else:
                    print(guess + "is not in the word.")
        else:
            print("\n You are out of guesses.  The correct word was:" + word)

            
            if guess not in lettersguessed:
                 lettersguessed.append(guess)

while True:
    word = choose_word()                 
    main(word)
    if input("Would you like to continue: ").lower().startswith("n"):
        break