"""
Name: Jonathan Neideigh
lab11.py
"""
from random import *


def get_words(words):
    filename = words
    infile = open(filename,"r")
    x = []
    for line in infile:
        x.append(line.strip())
    return x


def pick_word(words):
    rand_num = randint(0,len(words))
    return words[rand_num]


def guess_word(secret_word,guessed_letters,guessed_word,letter):
    check = False
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            guessed_word[i] = letter
            check = True
    if check == True:
        return True
    guessed_letters.append(letter)
    return False


def word_spelled(guessed_word, secret_word):
    if "".join(guessed_word) == secret_word:
        return True
    else:
        return False


def guess_letter(guessed_letters,turn_count,secret_word,guessed_word):
    letter = input("Enter a letter: ")
    letter = letter.lower()
    check = False
    while check == False:
        check = True
        for ch in guessed_letters:
            if letter == ch:
                print("This letter has already been chosen, try again.")
                letter = input("Guess a letter: ")
                letter = letter.lower()
                check = False
        if (len(letter) != 1) or not (ord(letter) >= 97 and ord(letter) <= 122):
            print("This is an invalid input, try again.")
            letter = input("Enter a letter: ")
            letter = letter.lower()
            check = False
    if guess_word(secret_word,guessed_letters,guessed_word,letter):
        return True
    else:
        return False


def print_board(guessed_word,turn_count,guessed_letters):
    print("--" + ("-----" * len(guessed_word)) + "--")
    print(guessed_word)
    print("--" + ("-----" * len(guessed_word)) + "--")
    print()
    print("Number of Guesses: " + str(turn_count))
    print("Guessed Letters: " + str(guessed_letters))
    print()


def play_game():
    words = get_words("wordlist.txt")
    secret_word = pick_word(words)
    guessed_word = ["_"] * len(secret_word)
    guessed_letters = []
    turn_count = 0
    print_board(guessed_word,turn_count,guessed_letters)
    while turn_count < 7 and not word_spelled(guessed_word,secret_word):
        if not guess_letter(guessed_letters,turn_count,secret_word,guessed_word):
            turn_count += 1
        print_board(guessed_word,turn_count,guessed_letters)
    if turn_count >= 7:
        print_board(guessed_word,turn_count,guessed_letters)
        print("Game Over!")
    else:
        print("You win!")


def main():
    play_game()
    pass


main()
