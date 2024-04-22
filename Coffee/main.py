# TODO: 1. Prompt user by asking what they would like or report to see whats there.
# TODO: 2. Turn off the Coffee machine by entering 'off' to the prompt.
# TODO: 3. Print a report of all the coffee machine resources.
# TODO: 4. Check to see if resources are sufficient.
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.
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
}
# Create smaller dictionary to read drink choice into


def resource_sufficient(drink):
    #Before we make the drink, let's add a check that validates we have enough
    #as we passed drink ingredients as key, pair values So let's use that. 
    for item in drink.keys():
        if drink[item] > resources[item]:
            return False

    #We have enough to make the item
    for item in drink.keys():
        resources[item] = resources[item] - drink[item]

    return True


def process_coins(drink):
    penny = .01
    nickel = .05
    dime = .10
    quarter = .25
    #let's default to 0 incase they just hit enter. 
    #we have not accounted for user type non numbers
    #can put try catch around input. 
    penny_count = float(input("Please enter number of pennies: ") or 0) * penny
    nickel_count = float(input("Please enter number of nickels: ") or 0) * nickel
    dime_count = float(input("Please enter number of dimes: ") or 0) * dime
    quarter_count = float(input("Please enter number of quarters: ") or 0) * quarter
    total = penny_count + nickel_count + dime_count + quarter_count
    change = total - drink['cost']
    #We need to accept that exact change is legit. 
    if change >= 0:
        print(f"Your change is ${math.ceil(change)}.")
    else:
        print("You didn't put enough money in.  No coffee for you!")



def user_selection():
        #menu is already a dict, we will use this to our advantage
        #unless user select off, we return true to get back to this menu
        user_input = input("What would you like to drink? Type 'espresso', 'latte', 'cappuccino'.  Type 'report' "
                           "to check the resources on the machine.  If you are the machine maintainer, type the "
                           "secret word to turn the machine off. ")
        if user_input in MENU.keys():
            drink = MENU[user_input]
            makeable = resource_sufficient(drink['ingredients'])
            if makeable:
                process_coins(drink)
            else:
                print('Sorry we can`t make that item')
        elif user_input == 'report':
            print(resources)
        elif user_input == 'off':
            return False
        else:
            print("Invalid input, no coffee for you!")

        return True

def main():
    make_coffee = True
    while make_coffee:
        make_coffee = user_selection()

if __name__ == '__main__':
    main()

