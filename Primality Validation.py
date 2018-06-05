# Primality Validation - Verifies if a number is prime

def prime_check (): # Checks whether user input is prime
    inpt_num = int(input("Enter A Number To Be Validated \n"))

    if inpt_num == 2: # 2 is a prime number
        print ("Number is Prime \n")
    elif inpt_num > 1:
        for num in range(2, inpt_num): # From 2 up till the inputted number
            if (inpt_num % num) == 0: # Calculates the remainder of each number, if it is 0
                print ("Number is Not Prime \n")
                break
            else:
                print ("Number is Prime \n")
                break
    elif inpt_num == 1: # 1 is a unique number
        print ("1 is a unique number \n")
    elif inpt_num < 1: # Negative numbers are not prime
        print ("Number is Not Prime \n")

while True: # Infinite loop
    prime_check ()
