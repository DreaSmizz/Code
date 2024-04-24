import random


user_input = int(input("Guess a number between 1 and 10: "))
computer_number = random.randint(1, 10)
number_guess = int(input("How many chances do you think you need? "))


def game_play(user_input, computer_number, number_guess):
    count = 0
    while number_guess > count:
        if computer_number == user_input:
            print("You win! Good job!")
        elif computer_number > user_input:
            count += 1
            number_guess -= 1
            print(f"Too low! You have {number_guess} left!  ")
            user_input = int(input("Guess a number between 1 and 10: "))
        elif computer_number < user_input:
            count += 1
            number_guess -= 1
            print(f"Too high! you have {number_guess} left! ")
            user_input = int(input("Guess a number between 1 and 10: "))
    print(f"Out of guesses! The number was {computer_number}.  Try again! ")

game_play(user_input, computer_number, number_guess)

