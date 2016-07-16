import random
from hangman_graphics import game_display, one_wrong, two_wrong, three_wrong,\
 four_wrong, five_wrong, six_wrong, seven_wrong, eight_wrong, lost, win, clear

words=[]


def easy_words(words):
    b=[]
    for item in words:
        if len(item)>=4 and len(item) <= 6:
            b.append(item)
    return b

def medium_words(words):
    b=[]
    for item in words:
        if len(item)>=6 and len(item) <= 8:
            b.append(item)
    return b

def hard_words(words):
    b=[]
    for item in words:
        if len(item)>=8:
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
    mode_select()
    #print(mode_select)




def mode_select():
    while True:
        mode_select=input("Please enter 1 for easy, 2 for medium, and 3 for hard: ")
        try:
            mode_select=int(mode_select)
        except ValueError:
            print("\nPlease enter a valid number")
        if mode_select == 1:
            easy_words(words)
        elif mode_select == 2:
            medium_words(words)
        elif mode_select == 3:
            hard_words(words)
        else:
            print("Please enter 1,2,or 3\n")





if __name__ == '__main__':
    main()
