import random
from hangman_graphics import game_display, one_wrong, two_wrong, three_wrong,\
 four_wrong, five_wrong, six_wrong, seven_wrong, eight_wrong, lost, win, clear
#come back and make this a line with PEP8

e_words = []
m_words = []
h_words = []
guesses = []
good_guesses = []


with open('/usr/share/dict/words', 'r') as f:
    for line in f:
        good = line.strip().lower()
        if len(good) >= 4 and len(good) <= 6:
            e_words.append(good)
        elif len(good) >= 6 and len(good) <= 8:
            m_words.append(good)
        elif len(good) >= 8:
            h_words.append(good)



def easy_mode(e_words):
    number = random.randrange(1, len(e_words))
    global word
    word = e_words[number]
    print("easy mode\n")
    # print(easy_count)
    #print(word)
    #print("\t"+ "_ " * len(word))




def medium_mode(m_words):
    number = random.randrange(1, len(m_words))
    global word
    word=m_words[number]
    print("Medium mode\n")
    # print(medium_count)
    #print(word)
    #print("\t"+ "_ " * len(word))


def hard_mode(h_words):
    number = random.randrange(1, len(h_words))
    global word
    word = h_words[number] 
    print("Hard Mode\n")
    # print(hard_count)
    #print(word)


def mode_select():
    while 1:
        mode_choice = input("\ntype 1 for easy, 2 for medium, 3 for hard: ")
        try:
            mode_choice = int(mode_choice)
        except ValueError:
            print("\nPlease enter a valid number\n")
        if mode_choice == 1:
            easy_mode(e_words)
            break
        elif mode_choice == 2:
            medium_mode(m_words)
            break
        elif mode_choice == 3:
            hard_mode(h_words)
            break
        else:
            print("Please enter 1,2,or 3")

def line():
    line = ['_'] * len(word)
    word_letters = list(word)

    for index, letter in enumerate(word_letters):
        if letter in good_guesses:
            line[index] = letter

    print('\t' + ' '.join(line))

def letter_select():
    b_counter = 0
    g_counter = 0
    mode_select()

    while has_more_guesses(b_counter, g_counter) and not has_guessed_word():
        bad_choice(b_counter)
        letter_choice = input("Please enter your guess: ")
        if len(letter_choice) > 1:
            print(" Please only type in one letter at a time")
            break
        guesses.append(letter_choice)
        #print(guesses)
        cat=False
        for letter in word:
            if letter == letter_choice:
                good_guesses.append(letter)
                g_counter += 1
                cat=True
        if cat == False:
            b_counter+=1

        print(good_guesses)

    if has_guessed_word():
        win()
    else:
        lost(word)

def has_more_guesses(b_counter, g_counter):
    if b_counter + g_counter >= 8:
        return False

    return True

def has_guessed_word():
    for letter in word:
        if letter not in guesses:
            return False

    return True

def bad_choice(b_counter):
    clear()

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
        eight_wrong(word)

    line()



letter_select()
