"""
class Methods as Alternative Constructors in Python
"""
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def str_from(cls,String):
        return cls(String.split("-")[0],String.split("-")[1])

e1=Employee("Harry",12000)
print(e1.name)
print(e1.salary)

String="jony-12000"
e2=Employee.str_from(String)
print(e2.name)
print(e2.salary)



