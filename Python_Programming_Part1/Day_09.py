"""
typecasting in python
"""
#1)Explicit typecasting
string="7"
number=15
string_number=int(string)
sum=number+string_number
print(sum)

#2)Implicit typecasting
a=3
print(type(a))
b=3.0
print(type(b))
sum=a+b
print(sum)
print(type(sum))