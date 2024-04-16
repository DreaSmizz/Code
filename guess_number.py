#Choose random number between 1 and 100.
#Make function to set difficulty
#Take user through guessess

import random

number = random.choice(range(0,100))
user_guess = int(input("Guess a number between 1 and 100: "))
game_level = input("Choose a difficulty level, Type 'easy' or 'hard': ")
print(f"You picked {user_guess} and {game_level}, Good luck!")

if game_level == 'easy':
    chance = 10
    while chance > 0:
        if user_guess == number:
            print("You win")
        elif user_guess > number:
            chance -= 1
            print("Too high! ")
            user_guess = int(input("Guess again! "))
        else:
            chance -= 1
            print("Invalid input! ")
    print(f"Out of chances, number was {number}, you lose!")
elif game_level == 'hard':
    chance = 5
    while chance > 0:
        if user_guess == number:
            print("You win")
        elif user_guess > number:
            chance -= 1
            print("Too low! ")
            user_guess = int(input("Guess again! "))
        else:
            chance -= 1
            print("Invalid input! ")
    print(f"Out of chances, number was {number}, you lose!")
else:
    print("Invalid choice!! Good Day!")
    

