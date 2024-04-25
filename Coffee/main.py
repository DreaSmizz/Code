# TODO: 1. Prompt user by asking what they would like or report to see whats there.
# TODO: 2. Turn off the Coffee machine by entering 'off' to the prompt.
# TODO: 3. Print a report of all the coffee machine resources.
# TODO: 4. Check to see if resources are sufficient.
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.
# TODO: 8. Go back and add resource check in 1 month, fix code so that coin amount in machine prints also.
# TODO: 9. Build in logic that if user does not put enough money in, machine returns money
import math

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
    "profit": 0,
}
# Create smaller dictionary to read drink choice into


def resource_sufficient(user_input, drink):
    if (drink['ingredients']['water'] > resources['water'] and (drink['ingredients']['coffee'] > resources['coffee'])):
        print('Not enough resources to make coffee')
        return resources
    if user_input == 'espresso':
        resources['water'] = resources['water'] - drink['ingredients']['water']
        resources['coffee'] = resources['coffee'] - drink['ingredients']['coffee']
    else:
        resources['water'] = resources['water'] - drink['ingredients']['water']
        resources['milk'] = resources['milk'] - drink['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - drink['ingredients']['coffee']
    return resources


def process_coins(drink):
    #profit = resources['profit']
    penny = .01
    nickel = .05
    dime = .10
    quarter = .25
    penny_count = float(input("Please enter number of pennies: ")) * penny
    nickel_count = float(input("Please enter number of nickels: ")) * nickel
    dime_count = float(input("Please enter number of dimes: ")) * dime
    quarter_count = float(input("Please enter number of quarters: ")) * quarter
    total = penny_count + nickel_count + dime_count + quarter_count
    profit += total
    change = total - drink['cost']
    if change > 0:
        print(f"Your change is ${math.ceil(change)}.")
    else:
        print("You didn't put enough money in.  No coffee for you!")
    return profit


def main():
    make_coffee = True
    while make_coffee:
        user_input = input("What would you like to drink? Type 'espresso', 'latte', 'cappuccino'.  Type 'report' "
                           "to check the resources on the machine.  If you are the machine maintainer, type the "
                           "secret word to turn the machine off. ")
        if user_input == 'espresso':
            drink = dict(MENU['espresso'])
            resource_sufficient(user_input, drink)
            process_coins(drink)
        elif user_input == 'latte':
            drink = dict(MENU['latte'])
            resource_sufficient(user_input, drink)
            process_coins(drink)
        elif user_input == 'cappuccino':
            drink = dict(MENU['cappuccino'])
            resource_sufficient(user_input, drink)
            process_coins(drink)
        elif user_input == 'report':
            print(f"Water: {resources['water']}")
            print(f"Milk: {resources['milk']}")
            print(f"Coffee: {resources['coffee']}")
        elif user_input == 'off':
            make_coffee = False
        else:
            print("Invalid input, no coffee for you!")


if __name__ == '__main__':
    main()

#def espresso():
#    espresso_water = MENU['espresso']['ingredients']['water']
#    espresso_coffee = MENU['espresso']['ingredients']['coffee']
#    espresso_cost = MENU['espresso']['cost']
#    return espresso_water, espresso_coffee, espresso_cost
#def latte():
#    latte_water = MENU['latte']['ingredients']['water']
#    latte_coffee = MENU['latte']['ingredients']['coffee']
#    latte_milk = MENU['latte']['ingredients']['milk']
#    latte_cost = MENU['latte']['cost']
#    return latte_water, latte_coffee, latte_milk, latte_cost
#    def cappuccino():
#    cappuccino_water = MENU['cappuccino']['ingredients']['water']
#    cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']
#    cappuccino_milk = MENU['cappuccino']['ingredients']['milk']
#    cappuccino_cost = MENU['cappuccino']['cost']
#    return cappuccino_water, cappuccino_coffee, cappuccino_milk, cappuccino_cost
#def drink_choice():
#    drink_choice = input("What would you like to drink? Type 'espresso', 'latte', 'cappuccino'.  Type 'report' to check "
#        "the resources on the machine.  If you are the machine maintainer, type the secret word to turn "
#        "the machine off. ")
#    if drink == 'espresso':
#        drink = dict(MENU['espresso'])
#    elif drink == 'latte':
#        drink = dict(MENU['latte'])
#    elif drink == 'cappuccino':
#        drink = dict(MENU['cappuccino'])
#    elif drink == 'report':
#        print(resources)
#    else:
#        print("Invalid input, no coffee for you!")
#    return drink
