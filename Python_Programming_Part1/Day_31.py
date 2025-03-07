"""
Sets in Python
1)set is unordered datatypes
2)In sets the item is seperated by commas
3)The items are enclosed with curly bracket
4)Duplicate items does not allowed
5)The set is Mutable datatype
"""
#Empty set
s={}
print(type(s))

s=set()
print(type(s))

#Example of sets
city={"Jalgaon","Dhule","Mumbai","Pune","Jalna"}
print(city)

info={"Carla",19,False,5.9,19}
print(info)

num={1,2,3,4,5,6,7,8,9,10,10,10}
print(num)
print("----------------------------------")


#Accessing Set items using for loop
cities={"Jalgaon","Dhule","Mumbai","Pune","Jalna"}
for city in cities:
    print(city)
print()

info={"Carla",19,False,5.9,19}
for value in info:
    print(value)
print()

num={1,2,3,4,5,6,7,8,9,10,10,10}
for n in num:
    print(n)
print()

