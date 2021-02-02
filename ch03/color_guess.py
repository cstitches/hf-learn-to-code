import random

colors = ['blue', 'red', 'green', 'orange', 'purple', 'yellow', 'pink']

color= random.choice(colors)

guess = ''

guesses = 0

guess = input('Guess my color! You can choose red, orange, yellow, green, blue, purple, or pink. ')

while guess != color:
    guesses = guesses + 1
    guess = input('Nope, guess again! ')

if guesses == 1:
    print('You got it! It took you', guesses, 'wrong guess.')
else:
    print('You got it! It took you', guesses, 'wrong guesses.')
