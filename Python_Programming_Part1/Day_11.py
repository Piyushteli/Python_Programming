"""
String Datatype in Python
"""
#Single line string
name="Harry"
print(name)

#String Concatanation
name="AKash"
surname="Sharma"
print(name+" "+surname)

print("Hello " + "World")

#Multiline string
a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua"""
print(a)

#Accessing Characters of string
#Accessing Characters of string using its index
name="College"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print("----------------------")
#Accessing Characters of String using for loop
for character in name:
    print(character)
print("---------------------")
w="welcome to wscubetech"
t=len(w)
print(t)
for i in range(t):
    print(w[i])
print()
w="welcome to wscubetech"
t=len(w)
print(t)
for i in range(t-1,-1,-1):
    print(w[i])
