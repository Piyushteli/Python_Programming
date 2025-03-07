"""
Slicing in python
[Start:Stop:Step]
"""
string1="Gate Smashers"
substr1=string1[5:10]
print(substr1)

substr2=string1[:10]
print(substr2)

substr3=string1[5:]
print(substr3)

substr4=string1[:]
print(substr4)

substr5=string1[-8:]
print(substr5)

substr6=string1[-8:-3]
print(substr6)

substr7=string1[5::2]
print(substr7)

substr8=string1[::-1]
print(substr8)

substr9=string1[5:12].upper()
print(substr9)


