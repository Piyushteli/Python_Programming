"""
Python Tuples
1)It is Ordered datatype
2)It is collection of same or different datatypes
3) The items are mainly seperated using commas and enclosed with parentheses
4)It is immutable datatype
5)It can allow the duplicate items
"""
tuple1=(1,2,2,3,4,5,6)
print(tuple1)

tuple2=("sparrow","Parrot","crow")
print(tuple2)

tuple3=(1,"tiger",2,"lion",3,"pune")
print(tuple3)

"""Tuple indexing
1)positive indexing 
2)Negative indexing
Accessing Tuple items using its values"""
tuple1=(1,2,2,3,4,5,6)
print(tuple1[0])

tuple2=("sparrow","Parrot","crow")
print(tuple2[1])

tuple3=("pune","Mumbai","kolhapur","Nagpur")
print(tuple3[-1])
print("-----------------------")
"""Tuples slicing"""
tuple1=(10,20,30,40,50)
print(tuple1[:])

tuple2=(100,200,300,400,500)
print(tuple2[1:4])

tuple3=("Mango","banana","orange","Apple")
print(tuple3[-3:])

tuple4=(5,10,15,20,25,30)
print(tuple4[::-1])