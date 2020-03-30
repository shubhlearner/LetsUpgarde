#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# In[5]:


#Bank Account

class BankAccount:
    def __init__(self, owner, balance=0.00):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):# For deposting the money
        
        self.balance += amount

    def withdraw(self, amount):#for withdrawing the money
        
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def get_balance(self):# check the balance
        
        return self.balance


def main():
    customer1 = BankAccount('Shubham')
    print(customer1.get_balance())
    customer1.deposit(100)
    customer1.withdraw(30)
    print("The balance available in customer 1 account is", customer1.get_balance())

    customer2 = BankAccount('Shekhar', 200)
    print("The balance available in customer 2 account is", customer2.get_balance())

if __name__ == "__main__":
    main()

    


# # Assignment 2

# In[3]:


#Volume and SUrface area of a Cone
import math
from math import sqrt
pi = math.pi
class cone:   
    def __init__(self, radius=0, height=0):
        self.radius = radius
        self.height = height
        
    def cone_volume(self, radius, height):
        return float(1/3 * pi * radius ** 2 * height)


    def cone_surface(self, radius, height):
        return float(pi * radius ** 2 + pi * radius * sqrt(height ** 2 + radius ** 2))  

def main():
    print(dir(cone))
    a = cone(5,10)
    radius = float(input("Radius:"))
    height = float(input("Height:"))
    
    print("Cone volume: %d" %(a.cone_volume(radius, height)))
    print("Cone surface area: %d" %(a.cone_surface(radius, height)))
#     input.cone_surface(5)
#     input.cone_volume(5)
    
if __name__ == "__main__":
    main()


# In[ ]:




