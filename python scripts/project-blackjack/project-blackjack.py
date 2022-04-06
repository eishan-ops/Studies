############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.



import random

#variable declaration
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]




#-function declaration here:
def player():
  player_draw_another_card = "y"
  while player_draw_another_card == "y":
    player_draw_another_card = input("Do you wish to draw another card? (y/n):  ").lower()
    if player_draw_another_card == "y":
      if sum(player_hand) >= 11:
        cards[0] = 1
      player_hand.append(random.choice(cards))
      print(f"player hand: {player_hand}")
      print(sum(player_hand))
      if sum(player_hand) > 21:
        return player_hand
  print(f"Total of your hand {sum(player_hand)}")
  cards[0] = 11
  return player_hand


def house(player_hand):
  while sum(house_hand) < 16 or sum(player_hand) > sum(house_hand):
    if sum(house_hand) >= 11:
      cards[0] = 1
    house_hand.append(random.choice(cards))
  return house_hand

def house_hand_viewer(house_hand):
  print(f"house hand - {house_hand}")
  print(f"total of house hand : {sum(house_hand)}")

def play_blackjack():

  #choosing initial hands for PLAYER
  for i in range(2):
    player_hand.append(random.choice(cards))
  if sum(player_hand) == 22:                  #making sure 11 is not selected twice making the sum 22
    player_hand[1] = 1
  print(f"player hand: {player_hand} - total: {sum(player_hand)}")
  
  #chooosing initial hand for HOUSE
  for i in range(2):
    house_hand.append(random.choice(cards))
  if sum(house_hand) == 22:                   #making sure 11 is not selected twice making the sum 22
    house_hand[1] = 1
  house_second_card = house_hand[1]
  house_hand[1] = "-"                         #Hiding the house 2nd card.
  print(f"house hand: {house_hand}")#- total: {sum(house_hand)}")
  
  #Checking for player BLACKJACK win 
  if sum(player_hand) == 21:
    print("****  YOU WIN by BLACK-JACK  ****")
    return
  else:
    player_hand_total = sum(player())    
  #Checking for house BLACKJACK win 
  house_hand[1] = house_second_card
  if sum(house_hand) == 21:
    print("****  HOUSE WIN by BLACK-JACK  ****")
  else:
  #continuing the game & calling house turn if player not lost yet..
  #declaring a winner
    if player_hand_total <= 21:
      house_hand_total = sum(house(player_hand))
      
      if house_hand_total > 21:
        print("You WIN! - house loses!")
      elif house_hand_total == player_hand_total:
        print("Its a draw...")
      elif house_hand_total > player_hand_total:
        print("House wins!")
      else:
        print("You WIN!")
      house_hand_viewer(house_hand)
    else:
      print("You Lose!")
      #house_hand_viewer(house_hand)
      print(f"Total of your hand {player_hand_total}")
    play = input("Do you wish to continue playing ?  (y/n) :  ").lower()
    if play == "y":
      return "y"
    else:
      return "n"



play = input("Do you wish to play BlackJack (y/n) ? --").lower()
while play == "y":
  player_hand = []
  house_hand = []
  play = play_blackjack()

