"""
String formatting in python
We have mainly use format method
1)name indexes:
2)numbered indexes:
3)empty placeholder:

we have mainly using f-string instead of formate method
"""
#1)name indexes:
name="My name is {fname} {lname}".format(fname="rohit",lname="Sharma")
print(name)
print("-----------------------")

#2)numbered indexes:
str="Welcome to {0} and {1}"
s=str.format("Maharastra","MP")
print(s)
print("--------------------")

#3)empty placeholder:
str="Roll No is {} and name is {} and age is {}"
s=str.format(199,"Mohit",20)
print(s)
print("-------------------")
name="My name is {fname} {lname}".format(fname="rohit",lname="Sharma")
print(name)

str=("My name is {name:>10}")
s=str.format(name="ankush")
print(s)
print()

str=("My name is {name:^10}")
s=str.format(name="ankush")
print(s)
print()

str=("My name is {name:<10}")
s=str.format(name="ankush")
print(s)
print("")

"""
f-string in python 
"""
print("f string in python")
name="manish"
age=25
print(f"Hello my name is {name} and age is {age}")

print(f"{30*2}")

price=45
print(f"for only {price:.2f} dollars")

