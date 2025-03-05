# 001 Installing Python Locally on Your Computer
# 002 Download PyCharm for Windows or Mac

# coffee machine
# 初始化咖啡机的资源和菜单
resources = {
    "water": 300,
    "milk": 200,
    "coffee_beans": 100,
    "money": 0
}

menu = {
    "espresso": {"water": 50, "milk": 0, "coffee_beans": 18, "price": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee_beans": 24, "price": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee_beans": 24, "price": 3.0}
}


def check_resources(coffee_type):
    """检查是否有足够的资源制作所选咖啡"""
    coffee = menu[coffee_type]
    for ingredient, amount in coffee.items():
        if ingredient != 'price' and resources.get(ingredient, 0) < amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True


def make_coffee(coffee_type):
    """制作咖啡并更新资源"""
    if not check_resources(coffee_type):
        return

    coffee = menu[coffee_type]
    for ingredient, amount in coffee.items():
        if ingredient != 'price':
            resources[ingredient] -= amount

    resources["money"] += coffee["price"]
    print(f"Here is your {coffee_type}. Enjoy!")


def report():
    """打印咖啡机的资源报告"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee Beans: {resources['coffee_beans']}g")
    print(f"Money: ${resources['money']}")


def take_money():
    """取走咖啡机的钱"""
    print(f"I've taken ${resources['money']}.")
    resources["money"] = 0


def start():
    """启动咖啡机，显示菜单并等待用户选择"""
    while True:
        print("\nAvailable coffee options:")
        for coffee_type in menu:
            print(f"{coffee_type.capitalize()} - ${menu[coffee_type]['price']}")
        print("Enter 'report' to view resources.")
        print("Enter 'off' to turn off the machine.")
        print("Enter 'take' to take the money.")

        choice = input("\nWhat would you like to do? ").lower()

        if choice == "off":
            print("Turning off the coffee machine.")
            break
        elif choice == "report":
            report()
        elif choice == "take":
            take_money()
        elif choice in menu:
            make_coffee(choice)
        else:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    # 启动咖啡机
    start()
