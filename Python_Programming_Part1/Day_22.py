"""
Function Arguments and Return Function
Types of Arguments
1)Default Arguments
2)Keyword Arguments
3)Required Arguments
4)Variable length Arguments
  1)Arbitary Arguments
  2)Keyword arbitary Arguments

return Statements
"""
#1)Default Arguments
print("1)Default Arguments")
def average(a=10,b=20):
    average=(a+b)/2
    print("The average is ",average)

average()
print("----------------------------")
#2)Keyword Arguments
print("2)Keyword Arguments")
def average(a,b):
    average=(a+b)/2
    print("The average is ",average)

average(a=50,b=100)
print("----------------------------")
#3)Required Arguments or (positional arguments)
print("3)Required Arguments")
def average(a,b):
    average=(a+b)/2
    print("The Average is ",average)

average(5,5)
print("-----------------------------------")

#4)Variable length arguments
#1)Arbitary Arguments  (Accesses the arguments in form of Tuples)
print("4)Variable length arguments")
print("1)Arbitary Arguments or *args")
def name(*name):
    print("HELLO",name)

name("Rahul","om","pune","Mumbai")

def name(*name):
    print("HELLO",name[0],name[1],name[2])

name("Rahul","om","pune","Mumbai")

def num(*num):
    print(num[0],num[1],num[2],num[3])

num(2,4,6,8,10)
print()

#2)Keyword Arbitrary Arguments (Accesses the arguments in form of Dictionary)
print("2)keyword arbitrary arguments or **kwargs")
def name(**name):
    print("Hello",name["fname"],name["mname"],name["lname"])
    print(type(name))

name(fname="Mohit",mname="Arun",lname="Patil")
print("--------------------------------------")

#return statements
print("return statements")
def name(fname,mname,lname):
    return "HELLO, " +fname+" "+mname+" "+lname

name=name("tushar","bapu","mali")
print(name)




