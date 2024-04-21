# TODO: 1. Prompt user by asking what they would like or report to see whats there.
# TODO: 2. Turn off the Coffee machine by entering 'off' to the prompt.
# TODO: 3. Print a report of all the coffee machine resources.
# TODO: 4. Check to see if resources are sufficient.
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.
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

drink_choice = input(
    "What would you like to drink? Type 'espresso', 'latte', 'cappuccino'.  Type 'report' to check "
    "the resources on the machine.  If you are the machine maintainer, type the secret word to turn "
    "the machine off. ")


turn_off = False


def espresso():
    espresso_water = MENU['espresso']['ingredients']['water']
    espresso_coffee = MENU['espresso']['ingredients']['coffee']
    espresso_cost = MENU['espresso']['cost']
    return espresso_water, espresso_coffee, espresso_cost


def latte():
    latte_water = MENU['latte']['ingredients']['water']
    latte_coffee = MENU['latte']['ingredients']['coffee']
    latte_milk = MENU['latte']['ingredients']['milk']
    latte_cost = MENU['latte']['cost']
    return latte_water, latte_coffee, latte_milk, latte_cost


def cappuccino():
    cappuccino_water = MENU['cappuccino']['ingredients']['water']
    cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']
    cappuccino_milk = MENU['cappuccino']['ingredients']['milk']
    cappuccino_cost = MENU['cappuccino']['cost']
    return cappuccino_water, cappuccino_coffee, cappuccino_milk, cappuccino_cost


def resource_sufficient():
    breakpoint()


def process_coins():
    penny = .01
    nickel = .05
    dime = .10
    quarter = .25
    penny_count = float(input("Please enter number of pennies: ")) * penny
    nickel_count = float(input("Please enter number of nickels: ")) * nickel
    dime_count = float(input("Please enter number of dimes: ")) * dime
    quarter_count = float(input("Please enter number of quarters: ")) * quarter
    total = penny_count + nickel_count + dime_count + quarter_count
    print(total)
    return total


def main():
    if drink_choice == 'espresso':
        espresso()
        process_coins()
    elif drink_choice == 'latte':
        latte()
        process_coins()
    elif drink_choice == 'cappuccino':
        cappuccino()
        process_coins()
    elif drink_choice == 'report':
        resource_sufficient()
    else:
        print("Invalid choice! No coffee for you!")


main()








