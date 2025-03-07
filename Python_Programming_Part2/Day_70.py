"""
Instance and Class Variables in Python
"""
class Employee:
    Company_name="Microsoft"                             #class variable

    def __init__(self,Ename,salary,age):
        self.Ename=Ename                                #Instance variable
        self.salary=salary
        self.age=age

    def showdetails(self):
        print(f"The Employee name is {self.Ename} and the salary is {self.salary} and the age is {self.age}")

obj=Employee("Akash",20000,30)
print(f"The Company name is {Employee.Company_name}")
obj.showdetails()
print("")

obj1=Employee("Kishan",30000,40)
print(f"The Company name is {Employee.Company_name}")
obj1.showdetails()

