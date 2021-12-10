import random


class choose_words:
    def __init__(self, words):
        self.words = words ["Python", "Programming", "Web Development", "Object Oriented","" ]
        word = random.choice(words).lower()
        return word


class word_in_progress:
    def __init__(self, words, guess):
        word_in_progress = ""
        for letter in words:
            if letter in guess:
                word_in_progress += letter
            else:
                word_in_progress += "*"
        return word_in_progress


