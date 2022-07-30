import random

"""Creating variables for the users."""
user_wins = 0
computer_wins = 0

"""Creating the flow process and conditions."""
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

random_num = random.randint(0, 2)
computer_pick = options[random_num]
print("Computer picked", computer_pick + ".")

"""Deciding who won"""
if user_input == "rock" and computer_pick == "scissors":
    print("You Won!")
    user_wins += 1

elif user_input == "paper" and computer_pick == "rock":
    print("You Won!")
    user_wins += 1

elif user_input == "scissors" and computer_pick == "paper":
    print("You Won!")
    user_wins += 1

        



