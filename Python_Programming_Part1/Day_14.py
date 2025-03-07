"""
if  Statement
if.....else Statement
if...elif...else Statement
nested if
"""
#if statement
age=int(input("Enter the Age: "))
if (age>18 ):
    print("You can apply for License")
print("Speed trills but kills")

#if...else statement
age=int(input("Enter the age : "))
if age>18:
    print("you can apply for License")
else:
    print("Itni jaldi bhi kya hai")

#if...elif.....else statement
handsome="false"
good_salary="true"
if handsome=="true" and good_salary=="true":
    print("you will marry with a super model")
elif handsome!="true" and good_salary=="true":
    print("you will marry with a beautiful girl")
elif handsome=="true" and good_salary!="true":
    print("you will marry with a girl")
else:
    print("Bhagwan Bharose!!")

#nested if
age=int(input("Enter the age: "))
own_car="false"
if (age>=18):
    if(own_car=="true"):
        print("Drive your car")
    else:
        print("Work hard & purchase a new car")
else:
    print("pehle bade to ho jao")





