"""
List Functions
1)sort()
2)reverse()
3)index()
4)count()
5)copy()

zip() function is used to iterate two lists at the same time

"""
l=[10,20,30,40,50]
l1=[1,2,3,4,5]
for a,b in zip(l,l1):
    print(a,b)
print("---------------------------")
#1)sort()
l=[2,4,6,8,5,9,8,7,2,4,]
l.sort()
print(l)
print("--------------------------------")
colours=["indigo","Blue","white","violet"]
colours.sort()
print(colours)
print("--------------------------------")
#print the list in descending order
l=[2,4,6,8,5,9,8,7,2,4,]
l.sort(reverse=True)
print(l)
print("--------------------------------")
colours=["indigo","Blue","white","violet"]
colours.sort(reverse=True)
print(colours)
print("--------------------------------")

#2)reverse()
l=[1,2,3,4,5,6,7,8,9]
l.reverse()
print(l)
print("----------------------------------")

#3)index()
l=[0,1,2,3,4,5,6,7,8,9]
print(l.index(2))
print("------------------------------------")

#4)count()
l=[1,2,3,4,6,7,8,4,5,5,5,6,6]
print(l.count(5))
print("-----------------------------------")

#5)copy()
l=["Blue","orange","Black","White"]
newlist=l.copy()
print(newlist)
print("--------------------------------------")
"""function for updating the list
6)insert()
7)append()
8)extend()"""
#6)insert()
l=[10,20,30,40,50]
l.insert(0,10)
print(l)

#7)append()
l=[100,200,300,400]
l.append(500)
print(l)

#8)extend()
colour1=["voilet","indigo","orange","red"]
colour2=["yellow","blue","green"]
colour1.extend(colour2)
print(colour1)

"""
function for to deleting the item from list
 9)del()
 10)pop()
 11)remove()
 12)clear()"""

#9)__delitem__()
list=[200,400,600,800]
print(list.__delitem__(2))
print(list)

#10)pop()
l=[5,10,15,20,25,30]
l.pop(2)
print(l)

#11)remove()
l=[2,4,6,8,10]
l.remove(6)
print(l)

#12)clear()
l=[3,6,9,12,15]
l.clear()
print(l)
print()

#concatenating two lists
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print(list1+list2)