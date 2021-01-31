import random


### Establish winner variable as a string
# will be 'computer', 'player' or 'tie'
winner = ''


### Generate computer's choice
# Computer randomly chooses between 3 options using a random integer
# Then the choice is converted to a string for readability.
# Why use randint and not random.choice with a list of the three options?

comp_choice = random.randint(1,3)

if comp_choice == 1:
    comp_choice = "rock"

elif comp_choice == 2:
    comp_choice = "paper"

elif comp_choice == 3:
    comp_choice = "scissors"

else:
    print("The computer is confused. The computer hurts itself in confusion.")

### For testing -- don't want player to see computer's choice
#print("The computer chooses", comp_choice)



### Get player's choice

player_choice = input("What's your play? rock, paper, or scissors? ")

print("You chose", player_choice, "and the computer chose", comp_choice)


### Check for invalid choice
# Need to make this loop back to input for player_choice



### Check for tie
# test if the computer's and player's choices are the same

if player_choice == comp_choice:
    winner = "neither, it's a tie"

### Check for winner
# only need to test for computer's wins; after ruling out ties, if computer doesn't win, player does.

elif comp_choice == 'rock' and player_choice == 'scissors':
    winner = 'computer'

elif comp_choice == 'paper' and player_choice == 'rock':
    winner = 'computer'

elif comp_choice == 'scissors' and player_choice == 'paper':
    winner = 'computer'

else:
    winner = 'player'


print("The winner is...", winner)
