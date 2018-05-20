# Rock Paper Scissors - Simulate A Game Of Rock Paper Scissors

import random # Import Random Module

RPS = ["R", "P", "S"] # Computer choices
r_sttmnt= "Computer picked rock!" # Computer choice statements stored as variables
p_sttmnt = "Computer picked paper!"
s_sttmnt = "Computer picked scissors!"

instructions = ("Instructions: \n" # Instructions to user
                "Enter 'R' for Rock \n"
                "Enter 'P'for paper \n"
                "Ener 'S' for scissors\n")
print (instructions)

def game():
    choice = input("Rock, Paper or Scissors? \n")
    choice = choice.upper().strip() # Convert input to uppercase and erase whitespace
    comp_choice = random.choice(RPS) # Randomly picks a value from the RPS array

    if choice not in RPS: # Validate whether input is in RPS aaray
        print ("Invalid Input: Retry \n")
    else:

        if choice.upper() == "R": # User choice is Rock
            if comp_choice == ("S"):
                print (s_sttmnt + "You win! \n")
            elif comp_choice == ("P"):
                print (p_sttmnt + "You lose... \n")
            elif comp_choice == ("R"):
                print (r_sttmnt + "You tied \n")

        if choice.upper() == "P": # User choice is Paper
            if comp_choice == ("R"):
                print (r_sttmnt + "You win! \n")
            elif comp_choice == ("S"):
                print (s_sttmnt + "You lose... \n")
            elif comp_choice == ("P"):
                print (p_sttmnt + "You tied \n")

        if choice.upper() == "S": # User choice is Scissors
            if comp_choice == ("P"):
                print (p_sttmnt + "You win! \n")
            elif comp_choice == ("R"):
                print (r_sttmnt + "You lose... \n")
            elif comp_choice == ("S"):
                print (s_sttmnt + "You tied \n")

while True: # Runs game in an infinite loop
    game()
