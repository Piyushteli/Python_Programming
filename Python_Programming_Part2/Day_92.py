"""
json(javascript object Notation) Module in Python:
    1)json is the text format data which used to stored the data.
    2)It is mainly used to storing and transferring data between the broswer and the server.

json mainly support 6 data types
1)string
2)number
3)boolean
4)null
5)object
6)array
"""
import json
data={"course_name":"python","fees":50000,"Duration":"6 Months"}

f=json.dumps(data)
print(type(f))
print(f)
print("-------------------")

#Converting JSON to python objects
d='{"name":"Roshan","course":"Data Science","Duration":"4 YEAR"}'

file=json.loads(d)
print(type(file))
print(file)
for a in file:
    print(a,file[a])




