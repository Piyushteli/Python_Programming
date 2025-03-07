"""
Exception Handling in Python:
Types of Exception handling
1)Built_in Exception       (1)try,2)except,3)else,4)finally)
2)User Defined Exception   (raisedException)

Built_in Exception
TYPES OF ERRORS
1)SyntaxError
2)ValueError
3)NameError
4)TypeError:Wrong Datatype operation
5)ZeroDivisionError
6)IndexError
7)KeyError
8)ModuleNotFoundError
9)ImportError:This arises due wrong import of a module
10)IoError:This error arise due to some input output issue
11)EofError: This arises due to reaching End of the file
12)KeyboardInterrupt

User Defined Exception
"""
try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    c=a/b
    print("Division=",c)
except:
    print("Divide by zero Error")
else:
    print("Program is executed successfully")
finally:
    print("I AM ALWAYS EXECUTED....")

print("----------------------------------")
n=input("Enter the number: ")
print(f"The Multiplication table of {n} is: ")
try:
    for i in range(1,11):
        print(f"{int(n)} * {i} = {(int(n)*i)}")
except:
    print("Invalid Input....")

print("Some IMP Lines")
print("End of Program")
print()

#Example 2
try:
    n=int(input("Enter the Number: "))

except ValueError:
    print(ValueError)

#user-defined exception
age=int(input("Enter the age"))
if age<0:
    raise Exception ("Age can't be Negative")
elif age>=18:
    print("You can give vote")
else:
    print("YOU ARE CHILD")