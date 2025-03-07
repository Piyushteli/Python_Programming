"""
Python While loop
If the condition is true then loop is executed
"""
#print the number
n=int(input("Enter the Number: "))
i=1
while (i<=n):
    print(i)
    i=i+1
print("-------------")

#Reverse Number series
n=int(input("Enter the Number: "))
while (n>0):
    print(n)
    n=n-1
print("--------------------------")

#sum of the number
n=int(input("Enter the Number: "))
sum=0
i=1
while(i<=n):
    sum=sum+n
    n=n-1
print(sum)

#table of Number
n=int(input("Enter the Number: "))
i=1
while (i<=10):
    product=n*i
    print(n,"*",i,"=",product)
    i = i + 1

#Reverse of number
n=int(input("Enter the number:"))
rev=0
while(n>0):
    rev=(rev*10)+n%10
    n=n//10
print(rev)

#palidrome number
n=int(input("Enter the Number: "))
rev=0
i=n
while (n>0):
    rev=(rev*10)+n%10
    n=n//10
if(rev==i):
    print("The number is palidrome")
else:
    print("The number is not palidrome")


#factorial of a Number
n=int(input("Enter the Number: "))
fact=1
while(n>0):
    fact=fact*n
    n = n - 1
print(fact)

#Sum of digits
n=int(input("Enter the Number: "))
sum=0
while(n>0):
    sum=sum+n%10
    n=n//10
print(sum)



