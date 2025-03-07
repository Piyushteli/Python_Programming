"""
3)Random Module in Python
Functions in random module
1)random.randint():This function returns the value between (1,10)
2)random.randrange():This function returns the value between (1,10) 10 is not included
3)random.choice()
4)random.random()
5)random.shuffle()
6)random.uniform()
"""
import random
print(random.randint(1,10))
print("-----------------------------")
print(random.randrange(1,5))
print("-----------------------------")
list=["jalna","jalgoan","Delhi","Manmad","Nashik"]
print(random.choice(list))
print("----------------------------------")

print(random.random())       #This returns between (0-1)
print("--------------------------------")
l=[10,20,30,40,50]
random.shuffle(l)
print(l)
print("--------------------------------------")
u=random.uniform(3,9)            #retuns the float value
print(u)
