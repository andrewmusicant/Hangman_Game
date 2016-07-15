import random
from hangman_graphics import game_display, one_wrong, two_wrong, three_wrong,\
 four_wrong, five_wrong, six_wrong, seven_wrong, eight_wrong,win
#come back and make this a line with PEP8

easy_words = []
medium_words = []
hard_words = []
guesses = []
good_guesses = []

with open('/usr/share/dict/words', 'r') as f:
    for line in f:
        good = line.strip().lower()
        if len(good) >= 4 and len(good) <= 6:
            easy_words.append(good)
        elif len(good) >= 6 and len(good) <= 8:
            medium_words.append(good)
        elif len(good) >= 8:
            hard_words.append(good)




def easy_mode(easy_words):
    number = random.randrange(1, len(easy_words))
    global word
    word = easy_words[number]
    print("easy mode\n")
    # print(easy_count)
    print(word)
    #print("\t"+ "_ " * len(word))




def medium_mode(medium_words):
    number = random.randrange(1, len(medium_words))
    word=medium_words[number]
    print("Medium mode\n")
    # print(medium_count)
    # print(word)
    print("\t"+ "_ " * len(word))


def hard_mode(hard_words):
    number = random.randrange(1, len(hard_words))
    word = hard_words[number]
    print("Hard Mode\n")
    # print(hard_count)
    # print(word)


def mode_select():
    while 1:
        mode_choice = input("\ntype 1 for easy, 2 for medium, 3 for hard: ")
        try:
            mode_choice = int(mode_choice)
        except ValueError:
            print("\nPlease enter a valid number\n")
        if mode_choice == 1:
            easy_mode(easy_words)
            break
        elif mode_choice == 2:
            medium_mode(medium_words)
            break
        elif mode_choice == 3:
            hard_mode(hard_words)
            break
        else:
            print("Please enter 1,2,or 3")

def letter_select():
    global b_counter
    b_counter = 0
    g_counter = 0
    mode_select()
    while b_counter <= 8:
        bad_choice()
        print("\t"+ "_ " * len(word))
        letter_choice = input("Please enter your guess: ")
        guesses.append(letter_choice)
        print(guesses)
        cat=False
        for letter in word:
            if letter == letter_choice:
                good_guesses.append(letter)
                g_counter += 1
                cat=True
        if cat == False:
            b_counter+=1
        if g_counter == len(good_guesses) and len(good_guesses) == len(word):
            win()
            break
        print(good_guesses)
    return



def bad_choice():
    if b_counter == 0:
        game_display()
    elif b_counter == 1:
        one_wrong()
    elif b_counter == 2:
        two_wrong()
    elif b_counter == 3:
        three_wrong()
    elif b_counter == 4:
        four_wrong()
    elif b_counter == 5:
        five_wrong()
    elif b_counter == 6:
        six_wrong()
    elif b_counter == 7:
        seven_wrong()
    elif b_counter == 8:
        eight_wrong()




letter_select()
