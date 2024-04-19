#Choose random number between 1 and 100.
#Make function to set difficulty
#Take user through guessess

import random



def setup_game():
    number = random.choice(range(0,100))

    return number

def set_chances():
    game_level = input("Choose a difficulty level, Type 'easy' or 'hard': ")
    print(f"You picked {game_level}, Good luck!")
    if game_level == 'easy':
        return 10
    return 5


def play_game(chance, number, winner=False):
    print(f"chances {chance}")
    if chance > 0:
        guess_number(chance, number)
    else:
        end_game(number, winner)
    
def end_game(number, winner):
    if (winner):
        print("You Win")
    else:
        print(f"Out of chances, number was {number}, you lose!")
    


def guess_number(chance, number):
    try:
        user_guess = int(input("Guess a number between 1 and 100: "))
        check_guess(user_guess,chance,number)

    except:
        print("Invalid Selection")
        guess_number(chance, number)
def check_guess(user_guess, chance, number):
    if user_guess == number:
        play_game(chance=0, number=number, winner=True)
        
    elif user_guess > number:
        chance -= 1
        print("Too high! ")
    elif user_guess < number:
        chance -= 1
        print("Too low!")
    else:
        chance -= 1
        print("Invalid input! ")
        
    play_game(chance, number)
    


def main():
    number = setup_game()
    chances = set_chances()
    play_game(chances, number)
    
if __name__ == '__main__':  
    main()
