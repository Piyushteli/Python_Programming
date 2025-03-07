"""
Getters and Setters in Python
"""

class Employee:
    def setid(self,id):
        self.id=id

    def getid(self):
        return self.id

    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name

obj1=Employee()
obj1.setid(101)
obj1.setname("Varun")
print(obj1.getid())
print(obj1.getname())
print("---------------------------")
class Player:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    @property
    def email(self):
        return (f"{self.fname}{self.lname}@gmail.com")

obj=Player("Ravi","patil")

obj1=Player("Ajay","mali")
print(obj.email)
print(obj1.email)

print("-------------------------------------------------")
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def explain(self):
        return (f"The employee name is {self.fname} {self.lname}")

    #Getter method
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set "
        return (f"{self.fname}{self.lname}@gmail.com")

    #setter method
    @email.setter
    def email(self,string):
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    #for deletion of the attribute
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

obj1=Employee("Nutan","Marathe")
print(obj1.explain())
print(obj1.email)

obj1.email="piyush.teli"
print(obj1.email)

del(obj1.email)
print(obj1.email)