import random
import sqlite3


def generate_pin():
    PIN = ""
    for i in range(4):
        PIN += str(random.randint(0, 9))
    return PIN


def log_into_account(card_number, pin_number):
    cur.execute("""SELECT number FROM card""")
    cards = cur.fetchall()
    found = False
    for card in cards:
        if card_number == card[0]:
            found = True
            cur.execute("""SELECT pin FROM card WHERE number = {}""".format(card_number))
            pin = cur.fetchone()[0]
            if pin == pin_number:
                print("You have successfully logged in!\n")
                return card[0]
            else:
                print("Wrong card number or PIN!\n")
                break
    if not found:
        print("Wrong card number or PIN!\n")


def generate_checksum(number):
    x = 0
    while (number + x) % 10 != 0:
        x += 1
    return x


def check_checksum(number):
    sum_ = 0
    list_ = list(number)
    for i in range(len(list_) - 1):
        if i % 2 == 0:
            list_[i] = int(list_[i]) * 2
            if int(list_[i]) > 9:
                list_[i] -= 9

        sum_ += int(list_[i])

    check = generate_checksum(sum_)
    if check == int(number[-1]):
        return True


def Luhn_algorithm():
    card = ""
    INN = "400000"
    sum_ = 0
    for i in range(8):
        card += str(random.randint(0, 9))
    card += "0"
    template = INN + card
    valid_number = list(template)
    for i in range(len(valid_number)):
        if i % 2 == 0:
            valid_number[i] = int(valid_number[i]) * 2
            if int(valid_number[i]) > 9:
                valid_number[i] -= 9

        sum_ += int(valid_number[i])

    checksum = generate_checksum(sum_)
    final = template
    final += str(checksum)
    return final


class Account:

    accounts = list()
    id_counter = 1

    def __init__(self):
        self.id = self.id_counter
        self.account_number = self.generate_a_number()
        self.pin = generate_pin()
        self.balance = 0
        self.accounts.append(self)
        self.id_counter += 1

        cur.execute("""INSERT INTO card VALUES (
        :id,
        :account_number,
        :pin,
        :balance
        )""", {"id": self.id, "account_number": self.account_number, "pin": self.pin, "balance": self.balance})
        connection.commit()

    def generate_a_number(self):
        while True:
            not_duplicate = True
            card_created = Luhn_algorithm()
            if card_created is None:
                continue
            else:
                cur.execute("""SELECT number FROM card""")
                cards = cur.fetchall()
                for i in range(len(cards)):
                    if card_created == cards[i][0]:
                        not_duplicate = False
                        break
            if not_duplicate:
                return card_created


class Console:

    def check_balance(self, account):
        cur.execute("""SELECT balance FROM card WHERE number = {}""".format(account))
        balance = cur.fetchone()[0]
        print("\nBalance: " + str(balance) + "\n")

    def make_transfer(self, account_from, account_to):
        cur.execute("""SELECT number FROM card""")
        cards = cur.fetchall()
        is_found = False
        for i in range(len(cards)):
            if account_to == cards[i][0]:
                is_found = True
                break
        if account_from == account_to:
            print("You can't transfer money to the same account!")
        elif not check_checksum(account_to):
            print("Probably you made a mistake in the card number. Please try again!")
        elif not is_found:
            print("Such a card does not exist.")
        else:
            cur.execute("""SELECT balance FROM card WHERE number = {}""".format(account_from))
            current_balance_from = cur.fetchone()[0]
            cur.execute("""SELECT balance FROM card WHERE number = {}""".format(account_to))
            current_balance_to = cur.fetchone()[0]
            print("Enter how much money you want to transfer:")
            transfer_amount = int(input())
            if transfer_amount > current_balance_from:
                print("Not enough money!")
            else:
                cur.execute("""UPDATE card SET balance = {} WHERE number ={}""".format(transfer_amount + current_balance_to, account_to))
                connection.commit()
                cur.execute("""UPDATE card SET balance = {} WHERE number ={}""".format(current_balance_from - transfer_amount, account_from))
                connection.commit()
                print("Success!")

    def menu(self):
        isRunning = True
        while isRunning:
            print("1. Create an account")
            print("2. Log into account")
            print("0. Exit")
            command = input()
            if command == "1":
                print("\nYour card has been created\nYour card number:")
                acc = Account()
                print(acc.account_number)
                print("Your card PIN:")
                print(acc.pin + "\n")
            elif command == "2":
                print("\nEnter your card number:")
                card_number_input = input()
                print("Enter your PIN:")
                pin_input = input()
                acc = log_into_account(card_number_input, pin_input)
                if isinstance(acc, str):
                    while True:
                        print("1. Balance")
                        print("2. Add income")
                        print("3. Do transfer")
                        print("4. Close account")
                        print("5. Log out")
                        print("0. Exit")
                        command = input()
                        if command == "1":
                            self.check_balance(acc)
                        elif command == "2":
                            print("\nEnter income:")
                            income = int(input())
                            cur.execute("""SELECT balance FROM card WHERE number = {}""".format(acc))
                            balance = cur.fetchone()[0]
                            cur.execute("""UPDATE card SET balance = {} WHERE number = {}""".format((income + balance), acc))
                            connection.commit()
                            print("Income was added!\n")
                        elif command == "3":
                            print("\nTransfer\nEnter card number:")
                            transfer_to = input()
                            self.make_transfer(acc, transfer_to)
                            print()
                        elif command == "4":
                            print("\nThe account has been closed!\n")
                            cur.execute("""DELETE FROM card WHERE number = {}""".format(acc))
                            connection.commit()
                            break
                        elif command == "5":
                            print("\nYou have successfully logged out!\n")
                            break
                        elif command == "0":
                            isRunning = False
                            break
            elif command == "0":
                print("\nBye")
                connection.close()
                isRunning = False


connection = sqlite3.connect("card.s3db")
cur = connection.cursor()
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='card' ''')
if cur.fetchone()[0] == 1:
    pass
else:
    cur.execute("""CREATE TABLE card (
    id INTEGER,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
    )""")
    connection.commit()

console = Console()
console.menu()
