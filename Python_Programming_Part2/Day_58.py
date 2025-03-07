"""
Constructor in python
    A Constructor is a special method in a class used to create and initialize an object of a class.

Types of Constructor
1)Default Constructor
2)Parameterized Constructor

"""
#1)Default Constructor
class Intro:
    def __init__(self):
        print("Welcome to Python Course")

obj=Intro()

#2)Parameterized Constructor
class person:
    def __init__(self,name,occupation):
        print("Hello")
        self.name=name
        self.occupation=occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person("Rajesh","Software Developer")
b=person("Sachin","Teacher")

a.info()
b.info()




