'''
This program is to check whether given number ius prime or not
'''
# Program to check if a number is prime or not
# To take input from the user
NUM=None
def primeornot():
    # prime numbers are greater than 1
    if NUM > 1:
    # check for factors
        for i in range(2, NUM):
            if (NUM % i) == 0:
                return "is not a prime number"
               
        else:
            return "is a prime number"
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return "is not a prime number"

def SETNUM(n):
    global NUM
    NUM=n