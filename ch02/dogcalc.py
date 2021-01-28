# solicit user's input for dog's name and age, return values stored as variables

dog_name = input("What is your dog's name? ")
dog_age = input("What is your dog's age? ")



# calculate dog's age in "human years"

    # unexpected result -- dog_age is treated as a string, not a number, replicates the string 7 times
    # human_age = dog_age * 7
    # need to convert string to integer

human_age = int(dog_age) * 7


