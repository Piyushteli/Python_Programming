"""
Local and global variables in python

"""

#Example 1
x=10   #global variable
def my_function():
    y=5          #local variable
    print(y)

my_function()
print(x)
#print(y)          #these will cause error because y is local variable
print("--------------------------------")


#Example 2
x=10     #global variable
def my_function():
    global x
    x = 5
    y = 5

    print(y)
my_function()
print(x)





