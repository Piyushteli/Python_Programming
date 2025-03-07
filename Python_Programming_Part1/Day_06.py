"""
Variables and datatypes in Python
"""
#Variables
a=3            #int
b=True         #Boolean
c="python"     #string
d=None         #None

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Memory Allocation
#Both variables has Same Address
a=10
b=10
print(a,b)
print(id(a))
print(id(b))

"""
Datatypes
Mutable datatypes
1)List
2)Dictionary
3)byte Array

immutable datatypes
1)Int
2)float
3)complex
4)string
5)Tuple
6)Set
"""
#1)Numerical data :- int,float,complex
m=2
print(m)
n=2.3
print(n)
p=6+2j
print(p)

#2)Text data:- Str
P="Parrot"
print(P)

#3)Boolean data:-(True ,False)
print(5<10)
print(20>50)


#4)Sequencing data :- List,Tuple
list1=[8,2.3,[-4,5],["apple","Mango"]]
print(list1)

Tuple1=(("parrot ,sparrow"),("lion","Tiger"))
print(Tuple1)

#5)Mapped data:- dict
dict={"name":"Mayur","age":20,"canvote":True}
print(dict)


