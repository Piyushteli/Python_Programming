"""
Break and continue  and Pass statements
Break and continue statements are mainly use in loop
pass statements is used as empty loop
"""
#1)Break statement
for i in range(5):
    if i==4:
        break
    print(i)

for i in range(1,101):
    print(i,end=" ")
    if i==50:
        break
    else:
        print("Missipie..")
        print("Thank you..")
print("\n------------------------------")

#2)Continue statement
list=[2,3,4,6,8,0]
for i in list:
    if i%2==0:
       continue
    else:
        print(i)
print()

#To get only odd numbers between 1-20
for i in range(21):
    if i%2==0:
        continue
    else:
        print(i)
print()

#To get only even numbers between 1-20
for i in range(21):
    if i%2!=0:
        continue
    else:
        print(i)

#3)pass statement
a=int(input("Enter the number: "))
if a>50:
    pass
else:
    print("Dataflair")
