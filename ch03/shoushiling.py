
### Set up
# import random functionality
# establish winner variable

import random

winner = ''


### Generate computer's choice
# computer randomly chooses between 3 options using a random integer
# then the choice is converted to a string for readability

comp_choice = random.randint(1,3)

if comp_choice == 1:
    comp_choice = 'rock'

elif comp_choice == 2:
    comp_choice = 'paper'

elif comp_choice == 3:
    comp_choice = 'scissors'

else:
    print('The computer is confused. It hurts itself in confusion.')


### For testing computer's choice

#print("The computer chooses", comp_choice)



### Get player's choice


player_choice = input('What\'s your play? rock, paper, or scissors? ')


### Check for invalid choice
# while the player's choice is NOT any valid option, reprompt
# `and` but not `or` because... 


while (player_choice != 'rock' and
       player_choice != 'paper' and
       player_choice != 'scissors'):
    player_choice = input('Sorry, you need to choose rock, paper, or scissors. ')



### Game logic

# test for tie

if player_choice == comp_choice:
    winner = 'tie'

# test if computer wins, otherwise player wins

elif comp_choice == 'rock' and player_choice == 'scissors':
    winner = 'Computer'

elif comp_choice == 'paper' and player_choice == 'rock':
    winner = 'Computer'

elif comp_choice == 'scissors' and player_choice == 'paper':
    winner = 'Computer'

else:
    winner = 'Player'


### Output the outcome
# message if tie, message if winner

if winner == 'tie':
    print('We both chose', comp_choice, 'play again.')
else:
    print(winner, 'won. The computer chose', comp_choice, 'and you chose', player_choice + '.')
