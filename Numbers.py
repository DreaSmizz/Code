"""Dice Game
Roll a pair of dice.
Add the values of the roll
Ask the user to guess a number.
Compare the user's guess to the total value
Determine winner, user or computer"""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Enter your guess: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The max value is: %d" % max_val
  user_guess = get_user_guess()
  if user_guess > max_val:
	  print "%d is an invalid choice, Try again" % user_guess
  else:
    print "Rolling..."
    sleep(2)
    print "The first value is: %d" % first_roll
    sleep(1)
    print "The second value is: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "The total is %d...." % total_roll
    print "Result..."
    sleep(1)
    if user_guess > total_roll:
      print "You won!!"
    else:
      print "Sorry Sucka!!"
  
roll_dice(6)
