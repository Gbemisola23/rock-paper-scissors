import random

"""Creating variables for the users"""
user_wins = 0
computer_wins = 0

"""Creating variables and conditions for users"""
options = ["rock", "paper", "scissors"]: 
while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
           break
    
    if user_input not in options:
        continue
"""rock: 0, paper: 1, scissors: 2"""
random_num = random.randint(0,2)
computer_pick = options[random_num]
print("Computer picked", computer_pick + ".")

"""Deciding who won"""
if user_input == 'rock' and computer_pick == 'scissors'
    print("You Won!")
    user_wins += 1
    continue



