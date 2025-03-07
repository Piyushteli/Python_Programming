"""
Super Keyword in Python
"""
class ParentClass:
    def parent_Method(self):
        print("This is the Parent class")

class ChildClass(ParentClass):
    def parent_Method(self):
        print("This")
        super().parent_Method()
        
    def child_Method(self):
        print("This is the child class")
        super().parent_Method()

Obj1=ParentClass()
Obj1.parent_Method()

Obj2=ChildClass()
Obj2.child_Method()
Obj2.parent_Method()
print("------------------------------------------")


"""
__init__ Method calling by using the super Keyword"""

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id


class Programmer(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary=salary

Emp=Employee("piyush",123)
print(Emp.name)

P=Programmer("Jayesh",231,30000)
print(P.name)
print(P.id)
print(P.salary)