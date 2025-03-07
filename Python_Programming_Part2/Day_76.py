"""
Polymorphism in Python:
    polymorphism means same object having different behaviour

There are two ways to perform polymorphism in python
1)Overloading:
    Method Overloading is the method having the same name with different arguments


2)Overriding:
    1)Method Overriding is the method having the same name with same arguments
    2)It is implemented with inheritance also
    3)It is mainly used for memory reducing processes
"""

"""Introduction"""
#Example 1  ("+" Operator)
print(5+5)             #addition
print("5"+"5")         #concatination

#Example 2  (len() Function)
print(len("Rohidas"))                     #counts character
print(len(["jalna","dhule","goa"]))       #counts string
print("--------------------------------")

#Method Overloading
class Area:
    def find_Area(self,a=None,b=None):
        if a!=None and b!=None:
            return ("Area :",a*b)
        elif a!=None:
            return ("SECOND: ",a*a)
        else:
            return ("Nothing....")

obj=Area()
print(obj.find_Area(2,10))
print(obj.find_Area(2))
print(obj.find_Area())


#Method Overriding
class A:
    def show_data(self):
        print("I am in A class")

class B(A):
    def show_data(self):

        print("I am in B class")

obj1=B()
obj1.show_data()

