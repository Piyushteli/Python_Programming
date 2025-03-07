"""
Python Function
Types of Function
1)Built in Function
i.e min(),max(),len(),sum(),range(),dict(),list(),tuple(),set(),print() etc

2)User defined Function
To create function mainly using def keyword
"""
#Creating function
def my_function():
    print("Hello from a function")

#Calling a function
def my_function():
    print("Hello from function")

my_function()

#Function without argument
def add():
    a=int(input("Enter the first Number: "))
    b=int(input("Enter the Second Number: "))
    c=a+b
    print("Addition is ",c)

add()
print("----------------------------")
def oddeven():
    n=int(input("Enter the Number: "))
    if (n%2==0):
        print("The Number is Even")
    else:
        print("The Number is odd")

oddeven()
print("-----------------------------")


#Function with one argument
def my_function(fname):
    print(fname,"Sharma")

my_function("Rohit")
my_function("Amol")

#function with more arguments
def my_function(fname,lname):
    print(fname,lname)

my_function("Virat","Kohli")

def name(fname,lname):
    print(fname,lname)

name("sahil","verma")

def name(fname,lname):
    print("Hello",fname,lname)

name("sam","Wilson")
print("---------------------")
def mean(a,b):
    mean=(a+b)/2
    print(mean)

mean(10,30)
print("-------------------------------")
def isgreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater")

def islesser(a,b):
    pass

isgreater(10,20)


c=100
d=90
isgreater(c,d)
print("-------------------------")

