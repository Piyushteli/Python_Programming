"""
Class Method in Python
    This method is mainly used to change the class variable
"""
class Employee:
    company="Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls,newCompany):
        cls.company=newCompany

e1=Employee()
e1.name="harry"
e1.show()

e1.changeCompany("Tesla")
e1.show()