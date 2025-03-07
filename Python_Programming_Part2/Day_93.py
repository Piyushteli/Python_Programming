"""
Writing and Reading JSON file
"""
import json
file=open("info.json","r")
f=file.read()

finaldata=json.loads(f)           #To convert the str datatype into dict datatype
for i in finaldata:
    print(finaldata[i])

print(type(finaldata))

