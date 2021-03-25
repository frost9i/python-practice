#!/usr/bin/env python3
import random
from sys import exit
#from replit import clear
#pip install pyyaml random_words
from random_word import RandomWords

clean_screen = lambda: print('\n'*100)

default_tries = 6
lives = default_tries
wins = 0
loses = 0
guess_list = []
word = ""

#words = ["baobab", "kangaroo", "english", "python", "apple"]
words = RandomWords().get_random_words(limit=15, includePartOfSpeech="noun", minLength=5, maxLength=10, sortBy="alpha", sortOrder="asc")
print(*words, "\n", sep=" ")

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def hangman_print():
    global lives
    state = -(lives + 1 - len(hangman))
    print(hangman[state])
    
def new_word():
    global word, lives, guess_list
    lives = default_tries
    guess_list = []
    
    word = random.choice(words).upper()
    for i in range(len(word)):
        guess_list.append("_")
    
    print("NEW HANGMAN GAME:\n")
    print("Guess the word:", "_ " * len(word))
    print("Lives:", lives)
    
def game():
    global lives, loses, wins, guess_list
    hangman_print()
    guess = input("Guess one letter at a time: ").upper()
    clean_screen()
    
    if len(guess) != 1:
        print("COMMON! ONE LETTER AT A TIME!")
        guess = ""
        #player_is_stupid = 1

    if guess in guess_list:
        #lives -= 1
        print(f"You guessed [{guess}] already. Lives left:", lives)
    elif guess in word and guess != "":
        print("Correct guess. Go on!")
    else:
        lives -= 1
        print("Wrong guess. Lives left:", lives)
            
    for i in range(len(word)):
        if guess == word[i]:
            guess_list[i] = word[i]
    
    # Too many incorrect tries
    if lives <= 0: # Lost
        loses += 1
        print("\nYou're out of lives.")
        hangman_print()
        print(*guess_list, sep=" ")
        print(*word, sep=" ")
        next_game()
    
    # Guessed all
    if not "_" in guess_list:
        wins += 1
        if wins >= 10:
            print(f"\n\nOMG! YOU ARE A HERO!\nWins: {wins}")
            print("\n\n...Now... Stop wasting your time.")
            exit()
        print("\nCongratulations! You won.")
        print(*word, sep=" ")
        next_game()
            
    print(*guess_list, sep=" ")
    game()

def next_game():
    #global lives, wins, loses, guess_list, word
    print("Wins:", wins, "\t", "Loses:", loses)
    again = input("\nDo you want to play again? Y/N ").lower()
    if again == "y":
        new_word()
        game()
    else:
        exit()

new_word()
game() 
            
        
