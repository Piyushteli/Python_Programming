"""
Raising Custom errors in python
"""
n=int(input("Enter the Number which is in between 1 to 100: "))
if (n<1 or n>100):
    raise ValueError("The number is not in between 1 to 100")
