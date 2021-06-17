# 1. Name: 
#    -Baden Hanchett-
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    -This program is meant to  display a message on the screen, 
#     prompt the user for information, make a decision, store 
#     data in a list, and loop. It will also say if the user 
#     input is too high or too low. and then output a list-
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part of the assignment was understanding the syntax
#    of python, I did a lot of programming in C++ before so I understand
#    how loops and lists and prints work but the speicifics of how 
#    you actually tell python what to do was the hardest to pick up
#    on. For example that there needs to be a colon after the while 
#    loop declaration but in C++ you just use (), so that was the most
#    difficult. And then also making sure the prints were output in
#    the correct format, such as when to add a new line for example. I did 
#    not find an especially difficult bug as this assignment was a 
#    review of concepts I already understood. I did not have difficulty
#    with the instructions, the comments in the template were helpful. 
# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program was about 2.5 hours-  

import random

# Game introduction
print ('\nThis is the "guess a number" game.')
# Prompt the user for how difficult the game will be. Ask for an integer
print ('You try to guess a random number in the smallest number of attempts.\n')
value_max = int(input('Pick a positive integer: '))
# Generate a random number between 1 and the chosen value
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing
print('Guess a number between 1 and' , value_max , '.')
# Initialize the sentinal and the array of guesses
guesses = []
# Play the guessing game
number = int(0)
count = int(0)
    # Prompt the user for a number
while value_random != number: 
    number = int(input()) 
    # Store the number in an array so it can be displayed later  
    guesses.append(number)
    count += 1
    # Make a decision: was the guess too high, too low, or just right
    if number > value_random: 
        print('\tToo high!')
    if number < value_random: 
        print('\tToo low!')    
# Give the user a report: How many guesses and what the guesses where
print ('You were able to find the number in', count , 'guesses.')
print ('The numbers you guessed were: {}\n'.format(guesses))