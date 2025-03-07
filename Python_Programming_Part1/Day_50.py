"""
Methods in file handling
read()
readline():-BY Default reads the first line
readlines():-reads multiple lines from file
writelines():-write the group of string in file
"""
#Example 1
f=open("asamplefile.py")
print(f.read(5))
print(f.read(5))
print("----------------------------")
for line in f:
    print(line)
print("----------------------------")

#Example 2
#for one line  (use readline() method )
f=open("asamplefile.py")
print(f.readline())
print("------------------------")

#for multiple lines   (use readlines() method )
f=open("asamplefile.py")
print(f.readlines())
print("---------------------------------")


#Example 3
f=open("asamplefile.py",'a')
list=[" Raj"," Ramesh"," sanket"," Mohit"]
f.writelines(list)
f.close()
print("-----------")

#for Reading
f=open("asamplefile.py")
print(f.readlines())




