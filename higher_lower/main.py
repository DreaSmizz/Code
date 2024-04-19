# Import and print logo from art file
# Import and print vs from art file
# Import random module
# Import clear function from replit
# Import game_data file
import random
from art import logo
from art import vs
from replit import clear
from game_data import data

print(logo)

def compare(a, b):
  user_choice = input('Who has more followers? Type "A" or "B": ')
  keep_going = True
  score = 0
  while keep_going:
    if user_choice == "A":
      if a["follower_count"] > b["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
        b = random.choice(data)
        print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
        print(vs)
        print(f'Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}.')
        choice = input('Who has more followers? Type "A" or "B": ')
      elif a["follower_count"] < b["follower_count"]:
        print(f"Wrong, final score {score}")
        keep_going = False
        clear()
    elif user_choice == "B":
      if b["follower_count"] > a["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
        a = random.choice(data)
        print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
        print(vs)
        print(f'Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}.')
        choice = input('Who has more followers? Type "A" or "B": ')
      elif b["follower_count"] < a["follower_count"]:
        print(f"Wrong, final score {score}")
        keep_going = False
        clear()
    else:
      print("Whoops, random didn't work for us.  Let's generate a new one.")
      a = random.choice(data)
      b = random.choice(data)
      print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
      print(vs)
      print(f'Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}.')
      choice = input('Who has more followers? Type "A" or "B": ')

def main():
  a = random.choice(data)
  b = random.choice(data)
  print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
  print(vs)
  print(f'Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}.')
  compare(a, b)

main()



# Print first person to compare
# print vs
# Print second person to compare
# Ask user to guess who has more followers
# Compare follower count of first person and second person
# If correct, add 1 and print and continue
# If wrong print final score and end gamea


