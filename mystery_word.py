import random
from hangman_graphics import game_display, one_wrong, two_wrong, three_wrong,\
 four_wrong, five_wrong, six_wrong, seven_wrong, eight_wrong, lost, win, clear

words=[]
guesses=[]


def easy_words(words):
    b=[]
    for item in words:
        if len(item) >=4 and len(item) <= 6:
            b.append(item)
    return b

def medium_words(words):
    b=[]
    for item in words:
        if len(item) >=6 and len(item) <= 8:
            b.append(item)
    return b

def hard_words(words):
    b=[]
    for item in words:
        if len(item) >= 8:
            b.append(item)
    return b

def random_word(words):
    number = random.randrange(0, len(words))
    b= words[number]
    return b

def display_word(words, guesses):
    line = ['_'] * len(words)
    word_letters = list(words)

    for index, letter in enumerate(word_letters):
        if letter in guesses:
            line[index] = letter.upper()
    return (' '.join(line))

def is_word_complete(words, guesses):
    for letter in words:
        if letter not in guesses:
            return False

    return True


def cleaned_words(words):
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            words.append(line.strip().lower())
    return words


def main():
    single_word = mode_select()
    while is_word_complete(single_word, guesses) != True:
        clear()
        game_display()
        print(single_word)
        print(display_word(single_word, guesses))
        letter_guess(single_word)

    win(single_word)


def mode_select():
    while True:
        mode_select=input("Please enter 1 for easy, 2 for medium, and 3 for hard: ")
        try:
            mode_select=int(mode_select)
        except ValueError:
            print("\nPlease enter a valid number")
        if mode_select == 1:
            easy_word = easy_words(cleaned_words(words))
            single_word = random_word(easy_word)
            return(single_word)
        elif mode_select == 2:
            medium_word = medium_words(cleaned_words(words))
            single_word = random_word(medium_word)
            return(single_word)
        elif mode_select == 3:
            hard_word = hard_words(cleaned_words(words))
            single_word = random_word(hard_word)
            return(single_word)
        else:
            print("Please enter 1,2,or 3\n")


def letter_guess(single_word):
    while True:
        letter_select= input("Please guess a letter you think is in the word: ")
        guesses.append(letter_select)
        break



if __name__ == '__main__':
    main()
