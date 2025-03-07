"""
Method Overriding in Python
"""
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def Area(self):
        return self.x*self.y

Obj1=Shape(3,5)
print(Obj1.Area())
print("---------------------------------")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)

    def Area(self):
        return 3.14*super().Area()

circle=Circle(5)
print(circle.Area())