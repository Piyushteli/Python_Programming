"""
Number Guessing using Random module
"""
import random
Cnumber=random.randrange(1,101)
user_input=int(input("Enter your Number: "))

if user_input > Cnumber:
    print("Computer Guess Number:", Cnumber)
    print("your guess Number is too high")
elif Cnumber > user_input:
    print("Computer Guess Number:",Cnumber)
    print("your guess Number is too low")
else:
    print("Computer Guess Number:",Cnumber)
    print("your guess Number is equal....")

