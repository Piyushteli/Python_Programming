"""
For loop with else statement
while loop with else statement
"""
for i in range(5):
    print(i)
else:
    print("The loop is terminated")
print("")

#example no2:-
for i in range(6):
    print(i)
    if i==4:
        break

else:
    print("Sorry no i")
print()

#Example number 3:
digits=[1,2,3,4,5]
for i in digits:
    print(i)
else:
    print("No element is left")
print()

#While loop with else
i=0
while(i<=10):
    print(i)
    i=i+1
else:
    print("loop is over..")
print()

#2)
n=int(input("Enter the Number: "))
i=1
while(i<=10):
    print(n,"*",i,"=",n*i)
    i=i+1
else:
    print("Table is printed..")