class CoffeeMachine:

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def state_of_machine(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print("$" + str(self.money) + " of money\n")

    def check_if_possible(self, water_needed, milk_needed, coffee_needed):
        if self.cups == 0:
            print("Sorry, not enough cups!\n")
            return False
        elif water_needed > self.water:
            print("Sorry, not enough water!\n")
            return False
        elif milk_needed > self.milk:
            print("Sorry, not enough milk!\n")
            return False
        elif coffee_needed > self.coffee:
            print("Sorry, not enough coffee!\n")
            return False
        else:
            print("I have enough resources, making you a coffee!\n")
            return True

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        command_buy = input()
        if command_buy == "1":
            if self.check_if_possible(250, 0, 16):
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.cups -= 1
        elif command_buy == "2":
            if self.check_if_possible(350, 75, 20):
                self.water -= 350
                self.coffee -= 20
                self.milk -= 75
                self.money += 7
                self.cups -= 1
        elif command_buy == "3":
            if self.check_if_possible(200, 100, 12):
                self.water -= 200
                self.coffee -= 12
                self.milk -= 100
                self.money += 6
                self.cups -= 1
        elif command_buy == "back":
            pass

    def fill(self):
        print("Write how many ml of water you want to add:")
        self.water += int(input())
        print("Write how many ml of milk you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans you want to add:")
        self.coffee += int(input())
        print("Write how many disposable coffee cups you want to add:")
        self.cups += int(input())
        print()

    def menu(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            command = input()
            print()
            if command == "buy":
                self.buy()
            elif command == "fill":
                self.fill()
            elif command == "take":
                print("I gave you " + str(self.money))
                self.money -= self.money
            elif command == "remaining":
                self.state_of_machine()
            elif command == "exit":
                break


machine = CoffeeMachine(400, 540, 120, 9, 550)
machine.menu()
