import random

from pygments.lexer import words

word = random.choice(['banana', 'abacate', 'uva', 'morango', 'laranja'])

chances = 7
count = 1

word_guessing = ["_" for i in word]
indices = []

start_index = 0

while count < chances:

    attempt = input("Guess a letter: ")

    if attempt in word:
        while True:
            index = word.find(attempt, start_index)
            if index == -1:
                break
            indices.append(index)
            start_index = index + 1  # Start search after the found substring

        for i in indices:
            word_guessing[i] = attempt

        indices = []

    print(word_guessing)
    if "_" not in word_guessing:
        break

    count += 1
