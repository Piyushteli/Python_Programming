"""
2)Multiple Inheritance
"""
class Employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"The Employee name is {self.name}")

class dance:
    def __init__(self,dance):
        self.dance=dance

    def Dance(self):
        print(f"The dance is {self.dance}")

class dancer(Employee,dance):
    def __init__(self,name,dance):
        self.name=name
        self.dance=dance

obj1=dancer("sandip","Kathak")
obj1.show()
obj1.Dance()

print("------------------------------------------------------")

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"The student name is {self.name} and age is {self.age}")

class Freelancer:
    def __init__(self,salary):
        self.salary=salary


    def info(self):
        print(f"The salary is {self.salary}")

class Boy(Student,Freelancer):
    def __init__(self,name,age,salary,experience):
        self.name=name
        self.age=age
        self.salary=salary
        self.experience=experience

    def details(self):
        print(f"The experience of that student is {self.experience} ")

obj1=Boy("Akash",23,10000,"1 Year")
obj1.show()
obj1.info()
obj1.details()
