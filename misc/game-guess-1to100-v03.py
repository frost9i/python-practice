#!/usr/bin/env

from random import randint

GUESS_NUMBER_MAX = 100
GUESS_NUMBER_TRIES_EASY = 10
GUESS_NUMBER_TRIES_HARD = 5

print("Welcome to Guess-the-number game!")

def guess_number_new():
  guess_number = randint(1, GUESS_NUMBER_MAX)
  print("\t\t\tPssst... number is: ", guess_number)
  return guess_number

def guess_difficulty():
  print("Select difficulty level:")
  print(f"Easy ({GUESS_NUMBER_TRIES_EASY} tries) or hard ({GUESS_NUMBER_TRIES_HARD} tries).")
  guess_user_diff = input("Enter 'e' or 'h': ")
  print(guess_user_diff.lower())
  if guess_user_diff.lower() == "h":
    print("Playing hard...")
    return GUESS_NUMBER_TRIES_HARD
  # elif guess_user_diff == "u":
  #   print("UNLIMITED MODE! You cheater.")
  #   return -1
  else:
    print("Take it easy...")
    return GUESS_NUMBER_TRIES_EASY

def guess_check(user_guess, guess_number):
  if user_guess == 0.1:
    print("\tYou wasted a try.")
  elif user_guess < 0 or user_guess > 100:
    print("\tNumber must be in range of 1 to 100.")
  elif user_guess < guess_number:
    print("\tToo small.")
  elif user_guess > guess_number:
    print("\tToo big.")
  elif user_guess == guess_number:
    print("\tEx-fucking-zactly! You guessed it.\n")
    return True
  else:
    print("\tWTF?")

def guess_user_guess():
  guess_user_input = input("Your guess: ")
  try:
    int(guess_user_input)
  except ValueError:
    print('\tPlease enter an integer.')
    return 0.1
  else:
    return int(guess_user_input)
  
  
def guess_game():
  guess_number = guess_number_new()
  guess_difficulty_tries = guess_difficulty()
  while guess_check(guess_user_guess(), guess_number) != True and guess_difficulty_tries > 1:
    guess_difficulty_tries -= 1
    print(f"\tTries left: {guess_difficulty_tries}")
  if guess_difficulty_tries == 0:
    print("\nOops! You're out of tries.")
  if input("Play again? (y/n): ").lower() == "y":
    print("NEW GAME")
    guess_game()

guess_game()
