"""
Static Method in python
    1)when using static method we are not using self as argument in function
    2)Not need to create the object or instance variable
"""
class Math:
    @staticmethod
    def Add(a,b):
     return a+b

obj=Math.Add(10,20)
print(obj)