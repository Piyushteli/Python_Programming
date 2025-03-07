"""
3)Multilevel Inheritance
"""
class SuperClass:
    def superclass(self):
        print("We are inside super class")

class DerivedClass1(SuperClass):
    def derivedclass1(self):
        print("We are inside derivedclass1")

class DerivedClass2(DerivedClass1):
    def derivedclass2(self):
        print("We are inside the derivedclass2")

obj1=DerivedClass2()
obj1.superclass()
obj1.derivedclass1()
obj1.derivedclass2()

#Example 2
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def show_details(self):
        print(f"Name:{self.name}")
        print(f"species:{self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed

    def show_details(self):
        Animal.show_details(self)
        print(f"breed:{self.breed}")

class GoldenRetrival(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="GoldenRetrival")
        self.color=color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color:{self.color}")

obj1=GoldenRetrival("Shera","Golden")
obj1.show_details()

print("-------------------------------------------------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"The Person name is {self.name} and his age is {self.age}")


class Employee(Person):
    def __init__(self, empid):
        self.empid = empid

    def info(self):
        Person.show(self)
        print(f"The empid is {self.empid}")


class Salary(Employee):
    def __init__(self, name, age, empid, salary):
        self.name = name
        self.age = age
        self.empid = empid
        self.salary = salary

    def detail(self):
        Employee.info(self)
        print(f"The Employee salary is {self.salary}")


obj1 = Salary("kiran", 23, 101, 20000)
obj1.detail()
