"""
Sets Methods in python
"""
#Joining Sets
#1)union() and update()
city_1={"Jalgaon","Dhule","Mumbai","Pune","Jalna"}
city_2={"Bhusawal","Shirpur","Nashik","Pune"}
city_3=city_1.union(city_2)
print(city_3)
print("-------------------------------------")

#update() function
city_1={"Jalgaon","Dhule","Mumbai","Pune","Jalna"}
city_2={"Bhusawal","Shirpur","Nashik","Pune"}
city_1.update(city_2)
print(city_1)
print(city_2)
print("-------------------------------------")

#2)intersection() and intersection_update()
name_1={"Sahil","Mohit","Rahul","Jayesh"}
name_2={"Mohit","Baban","Jayesh","Ravi"}
name_3=name_1.intersection(name_2)
print(name_3)


name_1={"Sahil","Mohit","Rahul","Jayesh"}
name_2={"Mohit","Baban","Jayesh","Ravi"}
name_1.intersection_update(name_2)
print(name_1)
print("---------------------------------------")

#3)symmetric_difference and symmetric_difference_update()
name_1={"Sahil","Mohit","Rahul","Jayesh"}            #That items which are not common in both sets
name_2={"Mohit","Baban","Jayesh","Ravi"}
name_3=name_1.symmetric_difference(name_2)
print(name_3)

name_1={"Sahil","Mohit","Rahul","Jayesh"}
name_2={"Mohit","Baban","Jayesh","Ravi"}
name_1.symmetric_difference_update(name_2)
print(name_3)
print("--------------------------------------------")

#4)difference() and difference_update()
city_1={"Tokyo","Madrid","Berlin","Delhi"}
city_2={"Seoul","Kabul","Delhi"}
city_3=city_1.difference(city_2)
print(city_3)

city_1={"Tokyo","Madrid","Berlin","Delhi"}
city_2={"Seoul","Kabul","Delhi"}
city_1.difference_update(city_2)
print(city_1)
print("---------------------------------------")

"""
Sets methods
1)isdisjoint()
2)issuperset()
3)issubset()
4)add()
5)update()
6)discard() or remove()
7)pop()
8)del()
9)clear()"""

#1)isdisjoint()
city_1={"Nashik","Pune","Mumbai"}
city_2={"Jalgaon","Nashik","Shirpur"}
print(city_1.isdisjoint(city_2))

city_1={"Nashik","Pune","Mumbai"}
city_2={"Jalgaon","Dhule","Shirpur"}
print(city_1.isdisjoint(city_2))
print("")

# 2)issuperset()
name_1={"Sachin","Akshay","Vishal"}
name_2={"Chetan","Aman","Akshay"}
print(name_1.isdisjoint(name_2))
name_3={"Sachin","Akshay","Vishal"}
print(name_1.issuperset(name_3))
print()

# 3)issubset()
num={1,2,3,4,5}
num1={1,2,5,6,7,8}
print(num1.issubset(num))
num2={1,2,3,4,5,7,8}
print(num.issubset(num2))
print()

# 4)add()
city={"Jalgaon","Dhule","Nashik","Mumbai"}
city.add("Surat")
print(city)
# 5)update()
city={1,2,3,4,5}
city_2={6,7,8,9,10}
city.update({11,22,43})
print(city)

# 6)discard() or remove()
city={"Jalgaon","Dhule","Nashik","Mumbai"}
city.discard("Pune")
print(city)

# city_1={"Jalgaon","Dhule","Nashik","Mumbai"}
# city_1.remove("Pune")
# print(city_1)

city={"Jalgaon","Dhule","Nashik","Mumbai"}
city.remove("Nashik")
print(city)


# 7)pop()
num={1,2,3,4,5}
num.pop()
print(num)


# 8)clear()
num={1,2,3,4,5}
num.clear()
print(num)



