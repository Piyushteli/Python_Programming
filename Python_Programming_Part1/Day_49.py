"""
File handling in python
Modes(r,w,x,a,t,b,+)
"""
#read command
f=open("asamplefile.py")
print(f.read())

#write command
f=open("asamplefile.py",'w')
f.write("India is the cleanest country")
f.close()

#appending command
f=open("asamplefile.py",'a')
f.write("and also the largest country")
f.close()



