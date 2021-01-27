# imports or makes available the functionality of randomness
import random

# creates 3 lists, where the list items are strings
# specifically, a list of 'verbs', a list of 'adjectives', and a list of 'nouns'
verbs = ['Leverage', 'Sync', 'Target',
         'Gamify', 'Offline', 'Crowd-sourced',
         '24/7', 'Lean-in', '30,000 foot']
adjectives = ['A/B Tested', 'Freemium',
              'Hyperlocal', 'Siloed', 'B-to-B',
              'Oriented', 'Cloud-based', 'API-based']
nouns = ['Early Adopter', 'Low-hanging Fruit',
         'Pipeline', 'Splash Page', 'Productivity',
         'Process', 'Tipping Point', 'Paradigm']

# creates a 'verb' variable, an 'adjective' variable, and a 'noun' variable
# the values are randomly selected from the coorespondingly-named lists
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# creates a 'phrase' variable that concatinates the random list items with spaces for human readiability
phrase = verb + ' ' + adjective + ' ' + noun + '.'

# outputs the resulting phrase variable to the screen5
print(phrase)
print('We\'re in marketing, baby!')
