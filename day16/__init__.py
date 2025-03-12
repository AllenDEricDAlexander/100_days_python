# OOP
class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, cups):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups

    def make_coffee(self, coffee_type):
        if coffee_type == "espresso":
            self.make_espresso()
        elif coffee_type == "latte":
            self.make_latte()
        elif coffee_type == "cappuccino":
            self.make_cappuccino()
        else:
            print("Invalid coffee type")

    def make_espresso(self):
        if self.water >= 50 and self.coffee_beans >= 10 and self.cups > 0:
            self.water -= 50
            self.coffee_beans -= 10
            self.cups -= 1
            print("Espresso is ready!")
        else:
            print("Not enough ingredients for Espresso!")

    def make_latte(self):
        if self.water >= 200 and self.milk >= 150 and self.coffee_beans >= 20 and self.cups > 0:
            self.water -= 200
            self.milk -= 150
            self.coffee_beans -= 20
            self.cups -= 1
            print("Latte is ready!")
        else:
            print("Not enough ingredients for Latte!")

    def make_cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 15 and self.cups > 0:
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 15
            self.cups -= 1
            print("Cappuccino is ready!")
        else:
            print("Not enough ingredients for Cappuccino!")

    def refill(self, water, milk, coffee_beans, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.cups += cups
        print("Machine refilled!")

    def status(self):
        print(f"Water: {self.water} ml")
        print(f"Milk: {self.milk} ml")
        print(f"Coffee Beans: {self.coffee_beans} g")
        print(f"Cups: {self.cups}")


# Example usage:
machine = CoffeeMachine(water=500, milk=300, coffee_beans=100, cups=5)

# Check status
machine.status()

# Make a coffee
machine.make_coffee("latte")

# Refill the machine
machine.refill(water=100, milk=50, coffee_beans=30, cups=3)

# Check status after refill
machine.status()

# Try making another coffee
machine.make_coffee("espresso")
