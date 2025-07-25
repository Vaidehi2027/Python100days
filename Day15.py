MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_on = True
def is_resources(order_ingredients):
    """Returns true if order can be made and false if order insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, we dont have enough of {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("pls insert coins!")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.10
    total += int(input("How many nickles?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    """Returns True when the payment is accepted,or False if money is insufficient!"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print (f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry you dont have enough money,your money hass been refunded!")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")

while is_on:
    choice = input("What would you like? (expresso,latte,cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

