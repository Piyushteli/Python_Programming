"""
Methods using (self) Argument in Python
It is acts as Reference variable
"""
#Example 1
class Demo:
    def name(self):
        print("Welcome to India")

obj=Demo()
obj.name()
print("---------------------------")

#Example 2
class DemoClass:
    a=10

    def showvalue(self):
        print(self.a)

demo=DemoClass()
demo.showvalue()
print("-----------------------------")

#Example 3
class DemoClass:
    a=10

    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)


obj=DemoClass()
obj.showvalue()
print("-----------------------------")

#using Multiple arguments
class Sum:
    def demo(self,a,b):
        print(a+b)

obj=Sum()
obj.demo(10,20)