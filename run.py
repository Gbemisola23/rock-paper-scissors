import random

"""Creating variables for the users"""
user_wins = 0
computer_wins = 0

"""Getting data from users"""
def options('rock', 'paper', 'scissors'): 
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


print("Goodbye!")


