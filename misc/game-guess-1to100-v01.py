#!/usr/bin/env

logo1 = '''
   ______                    
  / ____/_  _____  __________
 / / __/ / / / _ \/ ___/ ___/
/ /_/ / /_/ /  __(__  |__  ) 
\____/\__,_/\___/____/____/  
                             
   __  __                                  __             
  / /_/ /_  ___     ____  __  ______ ___  / /_  ___  _____
 / __/ __ \/ _ \   / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / / /  __/  / / / / /_/ / / / / / / /_/ /  __/ /    
\__/_/ /_/\___/  /_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                          
'''

from random import randint

def guess_game():
  global user_tries
  user_answer = int(input("Make a guess: "))
  user_tries -=1
  if user_tries != 0 and user_answer != number_x:
    if user_answer > number_x:
      print(f"Too high. Tries left: {user_tries}")
      guess_game()
    else:
      print(f"Too low. Tries left: {user_tries}")
      guess_game()
  if user_answer == number_x:
    print(f"Correct! Answer was: {number_x}")
  if user_tries == 0:
    print(f"Wrong, better luck next time. Answer was: {number_x}")

print("\nWelcome to the number guessing game!")
print(logo1)

while input("\nLet's play? Enter 'y': ").lower() == "y":
  difficulty = int(input("What difficulty do you want to play on?\n0 - for easy, 1 - for hard: "))

  if difficulty == 0:
    user_tries = 11
  else:
    user_tries = 6

  number_x = randint(1,100)
  print("\tRandint is: ", number_x)
  print("Guess the number between 1 and 100.\n")

  guess_game()

