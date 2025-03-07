"""
Inheritance in Python
    Inheritance allows a class(called child or derived class) to inherit attributes and methods from another class(called a parent class)
"""
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def Showdetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class programmer(Employee):
    def showlanguage(self):
        print("The default language is python")


obj1=Employee("Ramakant",502)
obj1.Showdetails()



obj2=programmer("Rahul",510)
obj2.Showdetails()
obj2.showlanguage()