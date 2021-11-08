import random


def read_input():
    random_string = ""
    range_ = 100
    print("Please give AI some data to learn...")
    print("The current data length is 0, 100 symbols left")
    print("Print a random string containing 0 or 1:\n")
    while len(random_string) < 100:
        input_string = input()
        for x in input_string:
            if x == "1" or x == "0":
                random_string += x
        if range_ - len(random_string) > 0:
            print("Current data length is {}, {} symbols left"
                  .format(len(random_string), range_ - len(random_string)))
            print("Print a random string containing 0 or 1:")
            print()

    print("Final data string:\n" + random_string + "\n")
    return random_string


def analyze_input(line):
    final_list = [line[i:i+4] for i in range(0, len(line))]

    triads = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0],
              "100": [0, 0], "101": [0, 0], "110": [0, 0], "111": [0, 0]}
    for x in final_list:
        if len(x) > 3 and x[0:3] in triads:
            if x.endswith("0"):
                triads[x[0:3]][0] += 1
            elif x.endswith("1"):
                triads[x[0:3]][1] += 1

    return triads


def start_game():

    print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")

    budget = 1000
    while True:
        print("\nPrint a random string containing 0 or 1:")

        test_string = input()
        if test_string == "enough" or budget <= 0:
            print("Game over!")
            break
        try:
            int(test_string)
        except ValueError:
            continue

        prediction_string = test_string[:3]
        for i in range(len(test_string) - 3):
            triplet = test_string[i:i+3]
            if len(triplet) > 2:
                if triads[triplet][0] > triads[triplet][1]:
                    prediction_string += "0"
                elif triads[triplet][0] < triads[triplet][1]:
                    prediction_string += "1"
                else:
                    prediction_string += str(random.randint(0, 1))

        counter = 0
        for i in range(len(test_string) - 3):
            if prediction_string[i] == test_string[i]:
                counter += 1
                budget -= 1
            else:
                budget += 1

        percentage = (counter / (len(test_string) - 3)) * 100
        print("prediction:\n" + prediction_string)
        print("\nComputer guessed right {} out of {} symbols ({:.2f}%)"
              .format(counter, len(test_string) - 3, percentage))
        print("Your capital is now ${}".format(budget))


line = read_input()
triads = analyze_input(line)
start_game()
