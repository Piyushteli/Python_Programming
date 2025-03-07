"""
python Dictionary
1)Dictonary is collection of key and values pair
2)Dictionary is ordered datatype
3)Dictionary store multiple items in single variable
4)Dictionary items are seperated by commas
5)items are enclosed with curly brackets
6)Dictionary is the Mutable datatype
"""
info={"name":"Karan","age":25,"eligible":True}
print(info)
print()

#Accessing dictonary items
#Accessing single values from dictonary
info={"name":"Karan","age":23,"Course":"Data science"}
print(info["name"])
print(info.get("name"))
print()

#Accessing multiple values
info={"name":"Karan","age":32,"Course":"Data science"}
print(info.values())
print()
#Accessing Keys
info={"name":"Karan","age":34,"Course":"Data science"}
print(info.keys())
print()
#Accessing key-value pairs
info={"name":"Karan","age":32,"Course":"Data Science"}
print(info.items())
print()