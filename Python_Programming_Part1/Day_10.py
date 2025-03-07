"""
Taking User input in Python
"""
variable=input()
print(type(variable))

a=input("Enter your name : ")
print("My name is ",a)
x=input("Enter the first Number: ")
y=input("Enter the Second Number: ")
sum=int(x)+int(y)
print(sum)


#For integers input
a=int(input("Enter the first Number: "))
b=int(input("Enter the Second Number: "))
sum=a+b
print(sum)

#For float input
a=float(input("Enter the first Number: "))
b=float(input("Enter the Second Number: "))
sum=a+b
print(sum)

#for any input
a=eval(input("Enter the first Number: "))
b=eval(input("Enter the Second Number: "))
sum=a+b
print(sum)




