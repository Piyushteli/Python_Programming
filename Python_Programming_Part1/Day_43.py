"""
HOW importing works in python
"""
#Examples
import math
result=math.sqrt(9)
print(result)
print("-----------------------------")

#1)from keyword
from math import sqrt
result=sqrt(9)
print(result)
print("------------------------------")

from math import sqrt,pi
result=sqrt(9)*pi
print(result)
print("------------------------------")


#2)importing everything
from math import *
result=sqrt(9)
print(result)
print("----------------------------------")

#3)The "as" keyword
import math as m
result=m.sqrt(9)
print(result)
print(m.pi)
print("------------------------------------")

#4)The dir function
import math
print(dir(math))
print("----------------------------------")
