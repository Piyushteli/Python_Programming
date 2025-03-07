"""
"is" VS "==" in python
"""
#is  :Indicates exact location of object in memory
#== :Indicates value

a="HELLO"             #string is immutable datatype
b="HELLO"
print(a is b)
print(a==b)
print("-------------------------")

a=12345
b=12345
print(a is b)
print(a == b)
print("---------------------------")

tuple1=("jalgaon","pune","Mumbai","Lonavala")
tuple2=("jalgaon","pune","Mumbai","Lonavala")
print(tuple1 is tuple2)
print(tuple1 == tuple2)
print("-----------------------------")

list1=["jalgaon","pune","Mumbai","Lonavala"]
list2=["jalgaon","pune","Mumbai","Lonavala"]
print(list1 is list2)
print(list1 == list2)

