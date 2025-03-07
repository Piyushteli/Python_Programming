"""
Magic /Dunder Method
Examples:
    1)__init__ method
    2)__str__ and __repr__ method :used to convert object to a string representation.
    3)__len__ method :It is mainly used to get length of an object
    4)__call__ method :This function is mainly used to make an object collable
"""
#1)__len__ Method
class Employee:
    def __init__(self,name):
        self.name=name

    def __len__(self):
       return len(self.name)

 #Output:<Day_73.Employee object at 0x0000020433C074D0>

# 2)__str__ and __repr__ method

    def __str__(self):
        return (f"The Employee name is {self.name} str")

    def __repr__(self):
        return (f"The Employee name is {self.name} repr")

#3)__call__Method
    def __call__(self):
        print("Employee is Lazy")




obj1=Employee("Raju")
print(len(obj1))
print((obj1))
print(repr(obj1))
obj1()