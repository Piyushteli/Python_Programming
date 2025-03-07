"""
Recursion in python
"""
#factorial of number
def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return(num*factorial(num-1))
num=5
print("Number:",num)
print("factorial is ",factorial(num))

#fibonacci series
def fibonacci(num):
    if num==0:
        return 0
    elif num==1 or num==2:
        return 1
    else:
        return((num-1)+num)

num=int(input("Enter the Number: "))
print("Number:",num)
print("Fibonacci series",fibonacci(num))