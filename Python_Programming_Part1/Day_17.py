#For loop for using iteration
name ="Piyush Teli"
for i in name:
    print(i)

Student="Abhishek"
for i in Student:
    print(i,end=",""\n")

#itering over a Dictionary
person={"name":"Alice","age":26,"city":"India"}
for key,value in person.items():
    print(f"{key}:{value}")

#loop over a list
colours=["Red","yellow","Blue","Orange"]
for colour in colours:
    print(colour)
print("----------------")

colours=["Red","yellow","Blue","Orange"]
for colour in colours:
    print(colour)
    for i in colour:
        print(i)

#list Comprehension
squares=[x**2 for x in range(1,11)]
print(squares)



#range function
"""
(start:stop:step)
"""
print("The Range Function")
for i in range(5):
    print(i)

for i in range (1,11):
    print(i,end=" ")
print("\n---------------")

print('Reverse Numbers')
for i in range (10,0,-1):
    print(i,end=" ")
print("\n----------------")

print("Table of a Number: ")
N=int(input("Enter the Number : "))
for i in range  (1,11):
    print(N ,"*", i ,"=", N*i)
print("------------------")

#string iterating using range function
str1="PYTHON"
t=len(str1)
for i in range(t):
    print(str1[i])


m=int(input("Enter the start no: "))
n=int(input("Enter the stop no: "))
z=n+1
for i in range (m,z):
    print(i)

#sum of numbers 1to10
sum=0
for i in range(1,11):
    sum=i+sum
print(sum)

#fibonacci Series
a,b=0,1
for i in range(10):
    print(a)
    a,b=b,a+b




