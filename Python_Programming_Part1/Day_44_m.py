"""
Call that module in this file
"""
#1)
import Day_44
print(Day_44.sum(10,20))
print(Day_44.mul(20,10))
print("--------------------")

#2)
from Day_44 import sum
print(sum(90,10))
print()

from Day_44 import mul
print(mul(90,10))
print("-----------------")

#3)
import Day_44 as m
print(m.sum(80,50))
print(m.mul(30,10))

i
