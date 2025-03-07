"""
Classes and Objects in Python

class:-
    A class is a blueprint or template for creating objects.It defines the Properties and methods of an Object

Object:-
    Object is the instance of the class used to access the Properties of the class Now lets create an object of the class

"""
#Creating a class
class Details:
    name="Rohit"
    age=20

#Creating an Object
obj1=Details()
print(obj1.name)
print("---------------------------")

#for Example of the Class and Object
class Details:
    name="Ramesh"
    age=20

obj1=Details()
print(obj1.name)
print(obj1.age)
print("------------------------------")

#2)Example
class person:                   #class define
    name="Ravi"
    occupation="Software Developer"
    Salary=25,000

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()            #Object define
b=person()
c=person()

b.name="Sahil"
b.occupation="Accountant"

c.name="Digamber"
c.occupation="HR"

a.info()
b.info()
c.info()