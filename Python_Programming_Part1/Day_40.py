"""
Enumerate function in python
"""
#Example 1
fruits=["Apple","Banana","Mango","Orange","Cherry","Lemon"]
for index,fruit in enumerate(fruits):
    print(index,fruit)
print("----------------------------")


#Example 2
fruits=["Apple","Banana","Mango","Orange"]
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)
print("----------------------------")


#Example 3
fruits=["Apple","Banana","Mango","Orange"]
for index,fruit in enumerate(fruits):
    print(f"{index+1}:{fruit}")
print("----------------------------------")

#Loop over the tuple
#Example 4
tuple=("Mumbai","Nashik","Pune","Surat")
for index,city in enumerate(tuple):
    print(index,city)
print("----------------------------------")

#Loop over the string
#Example 5
s="HELLO"
for index,character in enumerate(s):
    print(index,character)