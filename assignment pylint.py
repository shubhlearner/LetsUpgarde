'''
This program is to check whether given number is prime or not
'''

# To take input from the user
NUM = int(input("Enter a number: "))

# prime numbers are greater than 1
if NUM > 1:
   # check for factors
    for i in range(2, NUM):
        if (NUM % i) == 0:
            print(NUM, "is not a prime number")
            print(i, "times", NUM//i, "is", NUM)
            break
    else:
        print(NUM, "is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
    print(NUM, "is not a prime number")
    