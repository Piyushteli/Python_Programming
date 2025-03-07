"""
Short Hand if -else statements
If...Else in One Line
"""
a=2
b=330
print("A") if a>b  else print("B")

A=3300
B=330
print("A") if A>B else print("=") if A==B else print("B")

X=200
Y=500
print("X") if X>Y else print("=") if X==Y else print("Y")
C=10  if Y>X else 0
print(C)