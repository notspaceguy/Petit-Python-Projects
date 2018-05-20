# Dice Rolling Simulator - Simulates A Rolling Dice

import random # Import Random Module
import time # Import Time Module

def rand_roll (): # Rolls a number from 1-6
    roll = random.randint(1, 6)
    print ("Rolling...") # Appear to be loading
    time.sleep(1) # Loads program for 1 second
    print ("Dice Rolled " + str(roll))

rand_roll()
