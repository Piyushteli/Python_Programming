"""
Finally Clause in Python
Finally Clause is always executed
"""
try:
    num=int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer: ")
else:
    print("integer Accepted.")

finally:
    print("This block is always executed")


#finally clause is using mainly in function
def fun1():
    try:
        l=[2,4,5,8,]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0

    finally:
        print("I am always executed")

x=fun1()
print(x)





