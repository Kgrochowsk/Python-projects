import random
import string


def choose_word():
    list_of_words = ('python', 'java', 'kotlin', 'javascript')
    random_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
    return random_word


print("H A N G M A N\n")

word = choose_word()
guessed = set()
wrong_guessed = set()
counter = 0
menu_running = True
game_running = False

while menu_running:
    command = input('Type "play" to play the game, "exit" to quit: ')

    if command == 'play':
        game_running = True
        while game_running:

            for char in word:
                if char in guessed:
                    print(char, end="")
                else:
                    print("-", end="")

            letter = input("\nInput a letter: ")

            if len(letter) > 1:
                print("You should input a single letter\n")
                continue
            elif letter not in string.ascii_lowercase:
                print("Please enter a lowercase English letter\n")
                continue

            if letter in word and letter in guessed:
                print("You've already guessed this letter")

            if letter in word:
                guessed.add(letter)

            if letter not in word:
                if letter in wrong_guessed:
                    print("You've already guessed this letter")
                else:
                    wrong_guessed.add(letter)
                    print("That letter doesn't appear in the word")
                    counter += 1
                    if counter == 8:
                        print("You lost!")
                        game_running = False
                        break

            print()
            if set(word) == guessed:
                print(word)
                print("You guessed the word!\nYou survived!\n")
                game_running = False
                break
    elif command == "exit":
        menu_running = False
