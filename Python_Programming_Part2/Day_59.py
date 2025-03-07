"""
Python Decorators :
    Decorator is a function that takes another function as argument and returns a function
"""
#Example 1
def my_decorator(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@my_decorator
def hello():
    print("Hello world")

hello()
print("----------------------------------")

#Example 2
def greet(fx):
    def mfx(*args,**kwargs):
        print("Welcome user in sum function")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def sum(a,b):
    sum=a+b
    print(sum)

sum(1,2)
print("----------------------------")

#Another way calling
def greet(fx):
    def mfx(*args,**kwargs):
        print("Welcome user in sum function")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx


def sum(a,b):
    sum=a+b
    print(sum)

greet(sum)(10,20)
print("---------------------------------------")

def my_decorator(fx):
    def mfx():
        print("HELLO Good morning")

        fx()

        print("transaction successfully completed.. ")
    return mfx

@my_decorator
def payment():
    print("Transaction processing")

payment()









