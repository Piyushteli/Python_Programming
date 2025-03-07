"""
4)Hybrid Inheritance  in Python
    It is the combination of Multiple inheritance and single inheritance in object orinted programming
"""
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showdetails(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

class person(Human):
    def __init__(self,name,age,address):
        Human.__init__(self,name,age)
        self.address=address

    def showdetails(self):
        Human.showdetails(self)
        print(f"Address:{self.address}")

class program:
    def __init__(self,program_name,duration):
        self.program_name=program_name
        self.duration=duration

    def showdetails(self):
        print(f"program Name:{self.program_name}")
        print(f"duration:{self.duration} Months")

class student(person):
    def __init__(self,name,age,address,program):
        person.__init__(self,name,age,address)
        self.program=program

    def showdetails(self):
        person.showdetails(self)
        print(f"Program:{self.program}")


obj1=student("Dhruv",20,"Jalna","Data Science")
obj1.showdetails()

obj2=program("ML",6)
obj2.showdetails()