"""
-dir-dict-and-help-methods in Python
"""
#1)dir() method: The dir() function returns a list of all the attributes and methods (including dunder methods)

list=[10,20,30,40,50]
print(dir(list))

tuple=(10,20,30,40,50)
print(dir(tuple))
print("---------------------------------------------")

#2)__dict__ method: The __dict__ attribute returns a dictionary representation of an object attributes.
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p=Employee("John",30,50000)
print(p.__dict__)
print("----------------------------------------")

#3)help() Method: The help() function is used to get help documentation for an object.

print(help(Employee))