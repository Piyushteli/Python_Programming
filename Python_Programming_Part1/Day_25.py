"""
List in python
1)List is the ordered collection of data items
2)In List items are seperated by commas and enclosed by square brackets
3)list is the mutable datatype
4)list can contain duplicate items
"""
#Examples of list
list1=[1,2,2,4,3,3,4,5]
print(list1)

list2=["python","java","kotlin","php"]
print(list2)

list3=["python",1,3,"java",6,"php"]
print(list3)

"""
List Indexing
1)positive indexing
2)negative indexing 
"""
#Accessing the list
list1=["python","php","java","html"]
print(list1[0])
print(list1[3])
print(list1[2]) 

#negative indexing
print(list1[-1])
print(list1[-3])

"""
list slicing
[start:stop:step]
"""
list1=["Python","Java","php","javascript"]
sublist1=list1[::]
print(sublist1)

sublist2=list1[0:2]
print(sublist2)

sublist=list1[:-3]
print(sublist)

sublist3=list1[::-1]
print(sublist3)

sublist4=list1[-4:-1]
print(sublist4)

sublist5=list1[-1:-4:-1]
print(sublist5)

"""
List comprehesion
 """
#print numbers between 1 to 100 without using comprehension
l=[]
for i in range(1,101):
    l.append(i)
print(l)
print()
       
#print numbers between 1 to 100 without using comprehension
l=[i for i in range(1,101)]
print(l)
print()

#print even numbers between 1 to 100 without using comprehension
l=[i for i in range(1,101) if i%2==0]
print(l)
print()

#More examples
names=["Milo","Bruno","Anastasia","Rosa"]
name_with_o=[item for item in names if "o" in item]
print(name_with_o)

#Accepts items which have more than 4 letters
names=["Milo","Bruno","Anastasia","Rosa"]
l=[item for item in names if len(item)>4]
print(l)

#More Examples
Marks=[10,20,30,40,50]
new_list=[x+2 for x in Marks ]
print(new_list)

cube=[x**3 for x in range(10) if x%2==0]
print(cube)








