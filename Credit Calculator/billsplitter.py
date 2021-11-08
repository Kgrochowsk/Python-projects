import random

print("Enter the number of friends joining (including you):")

number_of_people = 0
is_correct = True
try:
    number_of_people = int(input())
    print()
    if number_of_people <= 0:
        print("No one is joining for the party")
        is_correct = False
except ValueError:
    print("No one is joining for the party")
    is_correct = False

if is_correct:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for i in range(number_of_people):
        name = input()
        friends[name] = 0
    print("\nEnter the total bill value:")
    bill = float(input())

    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    decision = input()
    if decision == "Yes":
        lucky_person = list(friends)[random.randint(0, len(friends) - 1)]
        print("\n{} is the lucky one!".format(lucky_person))
        for friend in friends:
            friends[friend] = round(bill / (len(friends) - 1), 2)
        friends[lucky_person] = 0
    elif decision == "No":
        for friend in friends:
            friends[friend] = round(bill / len(friends), 2)
        print("\nNo one is going to be lucky")

    print()
    print(friends)
