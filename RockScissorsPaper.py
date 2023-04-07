#Importing neccessary module
import random

#Welcome
print("Welcome to RockScissorPaper game!")

#Ask for player's name
player_name = input('What is your name?:').title()
print("Hello " + player_name + "!")

#Ask for player to input choice 
# Note GPT Correct: player_input = input("Please input R for Rock, S for scissors, P for paper:").upper()

while True:
    player_input = input("Please input R for Rock, S for scissors, P for paper:").upper()
    if player_input in ['R', 'S', 'P']:
        break
     
    print("Please enter a valid choice!!")

#MrBot probability choice list
probability = ['R', 'P', 'S']
mrbot_input = random.choice(probability)

#Convert short form into understandable form (To print out not for code)
moves_dict = {'R': 'Rock', 'S': 'Scissor', 'P': 'Paper'}

# Note error: player_choosed = moves_dict[player_input]
try:
    player_choosed = moves_dict[player_input]
except KeyError:
    player_choosed = "Invalid input"

mrbot_choosed = moves_dict[mrbot_input]  

#Store Both Players input
data = []
data.append(player_input)
data.append(mrbot_input)

#Print out Both player choice
print("You choosed " + '(' + player_choosed + ')')
print("MrBot choosed "+ '(' + mrbot_choosed + ')')
    
# create a dictionary of winning combinations
winning_combinations = {'R': 'S', 'S': 'P', 'P': 'R'}

# check for draw
if player_input == mrbot_input:
    print("Too bad! It's a draw!")
    
# check for winner
elif winning_combinations[player_input] == mrbot_input:
    print(f"Congratulations! {player_name} wins the game!")
else:
    print("MrBot wins the game!")