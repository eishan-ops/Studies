#importing modules for the game:
import random
from replit import clear
from art import logo
from art import vs
from game_data import data
print(logo)

#answer checker function declaration:
def check_answer(a , b, user_choice):
  if a["follower_count"] > b["follower_count"]:
    winner = "a"
  else:
    winner = "b"
  
  if user_choice == winner:
    return True
  else: 
    return False

#choosing a new_celebrity function declaration:
def choose_new_celebrity():
  print(vs)
  celebrity_b = random.choice(data)
  return celebrity_b
  

  
#randomly selecting 2 instagram profiles from game_data:
celebrity_a = random.choice(data)
print(f'{celebrity_a["name"]}, a {celebrity_a["description"]}, from {celebrity_a["country"]}')

celebrity_b = choose_new_celebrity()
print(f'{celebrity_b["name"]}, a {celebrity_b["description"]}, from {celebrity_b["country"]}')

#asking user for their First guess:
user_choice = (input("Who has more followers on instagram [type 'a' or 'b'] ? : ")).lower()


#defining a game_play:
score = 0
continue_game = True
while continue_game:
  if check_answer(a=celebrity_a, b=celebrity_b, user_choice=user_choice):
    score += 1
    clear()
    print(f"You are right! Current score : {score}")
    celebrity_a = celebrity_b
    print(f'{celebrity_a["name"]}, a {celebrity_a["description"]}, from {celebrity_a["country"]}')
    celebrity_b = choose_new_celebrity()
    print(f'{celebrity_b["name"]}, a {celebrity_b["description"]}, from {celebrity_b["country"]}')
    user_choice = (input("Who has more followers on instagram [type 'a' or 'b'] ? : ")).lower()
  else: 
    continue_game = False
    print("You lose :( ")
print(f"Your final score: {score}")

#-----------------------

# def user_win(a=celebrity_a, b=choose_new_celebrity()):
#   score += 1
#   replit.clear()
#   print(f"You are right! Current score : {score}")
#   celebrity_a = celebrity_b
#   print(f'{celebrity_a["name"]}, a {celebrity_a["description"]}, from {celebrity_a["country"]}')
#   print(f'{celebrity_b["name"]}, a {celebrity_b["description"]}, from {celebrity_b["country"]}')



