# Make sure all the files are in the same folder/directory
#####
# Python Hangman Game by TheRealMitch
#####
# Follow me on Github: https://github.com/TheRealMitch
#####
# Have fun
#####

from Art import colorfull_Logo, colorfull_Win, All_Win, You_Lose, stages
from colors import Colors
from clear import clear
import time

import random

colorfull_Logo()
Full_run = True
print(Colors.IGreen + Colors.Blink +
      "To quit enter \"quit\", \"poweroff\", \"shutdown\"" + Colors.Full_Reset)

quit = ["quit", "shutdown", "poweroff"]
levels = ["e", "h", "m", 'r']
pure_levels = ["e", "h", "m"]
levels_dict = {"h": "hard", "e": "easy", "m": "medium"}


while Full_run == True:

    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z',
    ]

    level = input(
        "type 'e' for easy(with definition), 'm' for medium, and 'h' for hard, and 'r' for random:\n")

    if level in quit:
        break

    while level not in levels:
        level = input("please choose your level of difficulty: ")

    if level in quit:
        break

    if level == 'r':
        level = random.choice(pure_levels)
        print(f"The level chosen is {levels_dict.get(level)}")
        time.sleep(1)

    if level == 'h':  # getting a word from the file hard.txt
        with open("hard.txt", 'r') as file:
            alltext = file.read().splitlines()
            chosen_word = random.choice(alltext).lower()
            letters = list(set(chosen_word))
    elif level == "e":
        with open('easy.txt', 'r') as file:  # Getting a word + the definition from the file easy.txt
            alltext = file.read().splitlines()
            full_word = random.choice(alltext)
            chosen_word = full_word.split(" ")[0]
            definition = " ".join(full_word.split(" ")[1:])
            letters = list(set(chosen_word))
    else:  # getting a word form medium.txt file
        with open("medium.txt", 'r') as file:
            alltext = file.read().splitlines()
            chosen_word = random.choice(alltext)
            letters = list(set(chosen_word))

    word_length = len(chosen_word)

    levels_hard = ['m', 'h']
    hints_easy = 1
    Hints = 3
    lives = 6
    strike = 0
    entered_letters = []
    display = []
    run_once = 0

    run = True

    if len(display) == 0:
        for i in range(word_length):
            display.append("_")

    if "-" in chosen_word:
        dash_position = chosen_word.index("-")
        display[dash_position] = "-"

    while run == True:

        if level == 'e' and len(entered_letters) == 0:
            clear()  # to clear the the print level at the first
            print(Colors.Bold +
                  f"Definition: {definition}" + Colors.Full_Reset + "\n")

        if set(display) == {"_"} and len(entered_letters) == 0 or set(display) == {"_", "-"}:
            if level == "h" or level == "m":
                clear()  # to clear the print at the first
            print(stages[lives].strip())
            print(" ".join(display) + "\n")
        if level in levels_hard:
            print("if you want to reveal a letter type 'reveal'." + Colors.Bold +
                  f"\tYou have {Hints} hint(s) left." + Colors.Full_Reset)
        else:
            print("if you want to reveal a letter type 'reveal'." + Colors.Bold +
                  f"\tYou have {hints_easy} hint(s) left." + Colors.Full_Reset)

        if level == "m" and run_once == 0:
            run_once += 1
            guess = random.choice(letters)
            letters.remove(str(guess))
        else:

            guess = input(Colors.Bold + "Guess a letter, " +
                          Colors.Full_Reset + "or 'random' for random:\n").lower()


        if guess in quit:
            break

        if guess not in ['reveal', 'random']:
            while guess.isdigit() == True or len(guess) != 1 or guess.isalpha() == False:
                guess = input("Guess a" + Colors.Blink + Colors.Bold +
                            Colors.Yellow_Dim + " LETTER: " + Colors.Full_Reset).lower()
                if guess in quit or guess in ['reveal', 'random']:
                    break

        if guess in quit:
            break

        if guess == 'reveal':
            if Hints > 0 and guess == "reveal" and level in levels_hard:
                Hints -= 1
                guess = random.choice(letters)
                letters.remove(str(guess))
            elif level == "e" and guess == "reveal" and hints_easy > 0:
                hints_easy -= 1
                guess = random.choice(letters)
                letters.remove(str(guess))
            elif hints_easy == 0 or Hints == 0:
                print("You don't have enough hints.")
                continue

        if guess == 'random':
            guess = random.choice(alphabet)
            print(Colors.Bold +
                  f"The random-picker picked: {guess}" + Colors.Full_Reset)
            time.sleep(1.25)

        if guess in entered_letters:
            print(Colors.Bold + Colors.Blink + Colors.Magenta +
                  f"You've already guessed {guess}" + Colors.Full_Reset)
            continue

        entered_letters.append(guess)

        alphabet.remove(str(guess))
        clear()

        for position in range(word_length):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = guess
                strike += 1

        if guess in chosen_word:
            left_to_guess = display.count("_")
            print(Colors.Cyan + Colors.Blink + "available letters:\n" +
                  Colors.Full_Reset + ",".join(alphabet))
            if level == 'e':
                print(Colors.Bold +
                      f"Definition: {definition}" + Colors.Full_Reset + "\n")
            print(stages[lives].strip() + "\n" + " ".join(display) + " You have " + Colors.Blink +
                  Colors.BIRed + Colors.Underlined + str(lives) + Colors.Full_Reset + " live(s) left." + "\n")

        if guess not in chosen_word:
            strike = 0
            lives -= 1
            print(Colors.Cyan + Colors.Blink + "available letters:\n" +
                  Colors.Full_Reset + ",".join(alphabet))
            if level == 'e':
                print(Colors.Bold +
                      f"Definition: {definition}" + Colors.Full_Reset + "\n")
            print(stages[lives].strip() + "\n" + " ".join(display) + " You have " + Colors.Blink +
                  Colors.BIRed + Colors.Underlined + str(lives) + Colors.Full_Reset + " live(s) left." + "\n")

        if lives == 0:
            run = False
            clear()
            time.sleep(0.5)
            print(f"the word was '{chosen_word}'")
            You_Lose()

        random_win = random.choice(All_Win)

        if "_" not in display:
            clear()
            colorfull_Win(random_win)
            time.sleep(0.5)
            print(f"the word was '{chosen_word}'")
            run = False

    repeat = input(
        "Type \"y\" if you want to replay, type 'n' for if you do not:\n")
    if "y" in repeat:
        Full_run = True
    else:
        Full_run = False
