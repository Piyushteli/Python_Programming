"""
Dictionary Methods
1)update()
2)clear()
3)pop()
4)popitem()
5)del()
"""
#1)update()
info={"name":"Karan","age":34,"Course":"Data Science"}
info.update({"eligible":True})
info.update({"Surname":"Sharma"})
print(info)

#2)Clear()
emp={"name":"raju","field":"Engineer","CGPA":7.4}
emp.clear()
print(emp)

#3)pop()
emp={"name":"raju","field":"Engineer","CGPA":7.4}
emp.pop("name")
print(emp)

#4)popitem()
emp={"name":"raju","field":"Engineer","CGPA":7.4}
emp.popitem()
print(emp)



