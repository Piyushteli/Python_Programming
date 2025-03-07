"""
Methods in file handling
1)seek():-to move the current position within a file to a specific point
2)tell():-returns the current position with in the file
3)truncate():-To truncate the file to a specific size
"""
#Example 1     seek() Method
with open("asamplefile.py") as f:
    #Move to the 10th byte in the file
    f.seek(10)
    data=f.read()
    print(data)
print("--------------------------------")

#Example 2      seek() Method
with open("asamplefile.py") as f:
    #Move to the 10th byte in the file
    f.seek(10)
    data=f.read(5)
    print(data)
print("--------------------------------")

#Example 3       seek() Method
with open("asamplefile.py") as f:
    #Move to the 10th byte in the file
    f.seek(10)
    data=f.readline()
    print(data)
print("-------------------------------")

#2)tell()  Method
with open("asamplefile.py") as f:
    f.seek(10)
    print(f.tell())
    f.seek(0)
    print(f.tell())
