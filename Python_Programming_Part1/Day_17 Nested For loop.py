#pattern printing
for i in range(1,6):
    print("*"*i)
print("----------")

"""
pattern printing using Nested Loop
"""
print("Printing the Stars Pattern : ")
for i in range (1,4):
    for j in range(1,6):
        print("*",end=" ")
    print()
print("\n-----------------------")
r=5
for i in range(1,r+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("\n------------------------")
r=5
for i in range(1,r+1):
    for j in range(i):
        print("*",end=" ")
    print()
print("\n--------------------")
r=5
for i in range(r,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print("\n----------------------")
print("The Number Pattern :")
r=5
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("\n----------------------")
r=5
for i in range(r,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print("\n-----------------------")
r=5
for i in range(1,r+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("\n----------------------------")
for i in range(5):
    for j in range(5-i-1):
        print(' ',end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print( )

for i in range(4,0,-1):
    for j in range(5-i):
        print(' ',end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print( )











