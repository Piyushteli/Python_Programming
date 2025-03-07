"""
5)Hierarchical Inheritance in Python
"""
class human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showdetails(self):
        print(f"NAME:{self.name}")
        print(f"age:{self.age}")

class Dad(human):
    def __init__(self,name,age,address):
        human.__init__(self,name,age)
        self.address=address

    def showdetails(self):
        human.showdetails(self)
        print(f"address:{self.address}")

class Mom(human):
    def __init__(self,name,age,address):
        human.__init__(self,name,age)
        self.address=address

    def showdetails(self):
        human.showdetails(self)
        print(f"Address:{self.address}")

class Son(Dad):
    def __init__(self,name,son_name,age,address):
        Dad.__init__(self,name,age,address)
        self.son_name=son_name
        self.age=age

    def showdetails(self):
        print(f"Dad_name:{self.name}")
        print(f"son_name:{self.son_name}")
        print(f"age={self.age}")

obj1=Son("Piyush","Jayesh",20,"Jalgaon")
obj1.showdetails()

obj2=Dad("Rahul",30,"panvel")
obj2.showdetails()

obj3=Mom("Mansi",25,"Kalyan")
obj3.showdetails()
print("-------------------------------------------------------------")

class Parent:
    def __init__(self, father_name, father_age):
        self.father_name = father_name
        self.father_age = father_age

    def info(self):
        print(f"Father name:{self.father_name}")
        print(f"Father Age:{self.father_age}")


class Son1(Parent):
    def __init__(self, father_name, father_age, name, age):
        Parent.__init__(self, father_name, father_age)
        self.name = name
        self.age = age

    def show(self):
        print(f"The Son1 name is {self.name}")
        print(f"The age is {self.age}")


class Son2(Parent):
    def __init__(self, father_name, father_age, sname, sage):
        self.father_name = father_name
        self.father_age = father_age
        self.sname = sname
        self.sage = sage

    def detail(self):
        print(f"The Son2 name is {self.sname}")
        print(f"The age is {self.sage}")


obj1 = Son1("Ravi", 50, "kishor", 23)
obj1.info()
obj1.show()
print()

obj2 = Son2("Ravi", 50, "Raj", 20)
obj2.info()
obj2.detail()






