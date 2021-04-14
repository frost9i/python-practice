#!/usr/bin/env
from random import choice
from time import sleep
from os import system

logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                 
                      |__/                  
'''

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_name = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

def card_hit():
  return choice(cards)

def new_game():
  global player, dealer
  player = []
  dealer = []
  player.append(card_hit())
  dealer.append(card_hit())
  player.append(card_hit())
  dealer.append(card_hit())
  ace_to_1(player)
  ace_to_1(dealer)

def print_cards():
  print(f"Your cards are: {player}. Your points: {sum(player)}")
  print(f"Dealer cards are: {dealer}. Dealer points {sum(dealer)}")
  
def check_cards():
  system('cls')
  if sum(player) == 21:
    if sum(dealer) != 21:
      print_cards()
      print("Blackjack! You win! You have 21 points.")
    else:
      print_cards()
      print("It's a draw.")
  elif sum(player) > 21:
    print_cards()
    print("You lost. Better luck next time...")
  elif sum(dealer) > 21:
    print_cards()
    print("You won!")
  elif sum(player) == sum(dealer):
    print_cards()
    print("It's a draw.")
  elif sum(player) < sum(dealer):
    print_cards()
    print("You lost.")
  elif sum(player) > sum(dealer):
    print_cards()
    print("You won!")
  else:
    print_cards()
    print("Something is wrong...")

def ace_to_1(user_cards):
  if 11 in user_cards and sum(user_cards) > 21:
    for i in range(len(user_cards)):
      if user_cards[i] == 11:
        user_cards[i] = 1

print("Welcome to CLI casino!\n")

while input("Play Blackjack? (y/n): ").lower()[0] == "y":
  system('cls')
  new_game()
  print(logo, "\n" * 2)
  print("New game. Shuffling...", "\n" * 2)
  sleep(1.5)
  print(f"Your cards are: {player}. Your points: {sum(player)}")
  print(f"One of dealer cards is: {dealer[1]}")
  
  while sum(player) < 21 and sum(dealer) != 21 and input("Hit or Stand? (h/s) ").lower()[0] == "h":
    print("Hitting...")
    sleep(1)
    player.append(card_hit())
    ace_to_1(player)
    
    print(f"Your cards are: {player}. Your points: {sum(player)}")

  while sum(dealer) < 17 and sum(player) < 22:
    dealer.append(card_hit())
    ace_to_1(dealer)

  print("Cheking cards...")
  sleep(1)
  check_cards()

print("Come back again!")