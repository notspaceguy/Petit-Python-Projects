# Number Guessing Game - User Has To Guess A Number

import random # Import random module

number = random.randint(1, 10) # Generates a random number from 1 - 10
correct = True

def guess_game (): # Prompts user to guess a number from 1 - 10
    while (correct == True): # Repeats until user guesses correct
        guess = int(input("Guess A Number From 1 - 10"))
        if (guess > number):
            print ("Guess Too High")
        elif (guess < number):
            print ("Guess Too Low")
        elif (guess == number): # If the user answers correctly
            print ("Correct Guess!")
            break # Terminate the loop

guess_game ()
