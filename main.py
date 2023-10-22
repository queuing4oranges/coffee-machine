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


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        is_enough = True
        # check if order ingredient at that particular key is greater than the resources using the SAME key
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False
        else:
            is_enough = True
        return is_enough


def process_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters: "))
    nickel = int(input("How many nickels: "))
    dimes = int(input("How many dimes: "))
    pennies = int(input("How many pennies: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickel * 0.05) + (pennies * 0.01)
    return total


def is_transaction_successful(money_received, drink_cost):
    # true when payment accepted, false when money insufficient
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Your change: {change}")
        # in order to reach variable 'profit', we need to access it:
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough dough. Money is refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    # deduct required resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True

while is_on:
    choice = input("Hi, what would you like to drink? espresso/latte/cappuccino?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f" You have")
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            # next step: process coins
            payment = process_coins()
            # check if the user has put in enough money - if yes, give them change and add money to profit, if not,
            # refund
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





















# TODO check that the resources are sufficient (if insufficient, cant make drink and give feedback to user)
# TODO process coins - when ordering it should ask of the quantity of each coins, which is:
#  quarters (0.25), dimes (), nickles (), pennies()
# TODO - calculate above and say that it cant make the drink if there are too little coins
#  (Sorry, that's not enough money, Money refunded.
# TODO - check if transition is successfull
# TODO - make coffee and deduct the resources



