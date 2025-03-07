"""
Types of Inheritance
1)Single Inheritance
2)Multiple Inheritance
3)Multilevel Inheritance
4)Hybrid Inheritance
5)Hierachical Inheritance

"""

#1)Single Inheritance
class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showdetails(self):
        print(f"The name is {self.name} and Age is {self.age}")

class child(Parent):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print(f"The name is {self.name} and age is  {self.age}")

obj1=Parent("Raju",55)
obj1.showdetails()

obj2=child("laksh",20)
obj2.details()
obj2.showdetails()

