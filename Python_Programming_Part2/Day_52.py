"""
Lambda function in Python
Syntax:
lambda arguments:expression
"""
def sum(a,b):
    c=a+b
    print(c)
sum(10,20)

#using lambda function
s=lambda a,b:a+b
print(s(50,50))
print("-------------------------------")

avg=lambda x,y:(x+y)/2
print(avg(10,30))

print("---------------------------------")
mul=lambda x,y:x*y
print(mul(5,10))
