"""
Encapsulation in Python
Access modifier/Specifier in python :-
    Python does not have any strict rules when it comes to public,private or protected like java
    It is just used for convenient for user
"""
"""
Types of Access Specifier/Modifiers
1)Public Modifier
2)Private Modifier
3)Protected Modifier
"""
class Demo:
    _a=10           #protected variable
    __b=20          #Private variable

    def show(self):
        print(f"The value of a:",self._a)
        print(f"The value of b:",self.__b)

obj=Demo()
obj.show()

#1)Public Modifier
class Student:
    def __init__(self,name,age):
        self.name=name               #public variable
        self.age=age

obj=Student("Lakhan",30)
print(obj.name)
print(obj.age)
print("------------------------------")

#2)Private Modifier
class Student:
    def __init__(self,age,name):
        self.__age=age                                 #private variable
        self.__name=name

obj=Student(20,"PIYUSH")
print(obj._Student__age)
print(obj._Student__name)
print("-----------------------")


#3)Protected access modifier
class Employee:
    def __init__(self):
      self._name="Harry"
      self._salary=50000

obj=Employee()
print(obj._name)
print(obj._salary)
print("-----------------------")

#Encapsulation  in Python
class A:
    __a=10       #private

    def show(self):
        print("The value of a =",self.__a)

obj=A()
obj.show()
print(obj.__a)




