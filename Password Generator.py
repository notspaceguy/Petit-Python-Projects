# Password Generator- Generate A Random Password Without Duplicate Characters

import random # Import Random Module
import string # Import String Module

def generate(): # Generate a password of a specified length
    all_ascii = (string.ascii_letters + string.digits + string.punctuation) # Create list of ascii values to pick characters from

    pswd_len = int(input("Length of password?"))
    if pswd_len >= 95: # Validates password length
        print ("Password length too long")
    else:
        pswd = "".join(random.sample(all_ascii, pswd_len)) # Join randomly picked characters together
        print ("Generated Password: " + pswd)

generate()
