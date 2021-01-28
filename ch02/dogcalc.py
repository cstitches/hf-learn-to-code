# Part 1 & 2: solicit user's input for dog's name and age, return values stored as variables

dog_name = input("What is your dog's name? ")
    # the preferred answer is "Dogmeat"

dog_age = input("What is your dog's age? ")



# Part 3: calculate dog's age in "human years"

    # unexpected result -- dog_age is treated as a string, not a number, replicates the string 7 times
    # human_age = dog_age * 7
    # need to convert string to integer

human_age = int(dog_age) * 7


# Part 4: output/print to user the dog's age in "human years"
# Convert human_age integer back to string for printing

    # Old method, concatenate the output together
    # print("Your dog " + dog_name + " is " + str(human_age) + " in human years.")

# Better method, pass multiple arguments separated by commas to print function; automatically includes a space between each arg

print( 'Your dog',
       dog_name,
       'is',
       str(human_age),
       'years old in human years.'
    )
