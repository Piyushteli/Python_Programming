"""
pickle Module in python
    storing the datatypes using pickle module
    1)Boolean
    2)Integers
    3)floats
    4)complex numbers
    5)strings
    6)Tuples
    7)Lists
    8)Sets and Dictionary

Function in pickle module
1)pickle.dump()  :This function is called to serialize(store) an object hierarchy
2)pickle.load() :This function is called to de-serialize(read) a data stream
"""
import pickle
example={"Name":"jayesh","roll_no":101,"Branch":"Data science"}

pickle_write=open("text.txt","wb")
pickle.dump(example,pickle_write)
pickle_write.close()


data=open("text.txt","rb")
print(pickle.load(data))
data.close()


