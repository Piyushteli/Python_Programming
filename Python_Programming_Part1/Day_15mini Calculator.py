print("Addition:'+'\n"
      "Subtraction:'-'\n"
      "Multiplication:'*'\n"
      "Division:'/'\n"
      "Remainder:'%'\n")
num1=int(input('Enter the First Number: '))
num2=int(input("Enter the Second Number: "))
opr=input("Enter the opr \"+,-,*,/,%\": ")
if (opr=="+"):
    print("Addition:",num1+num2)
elif (opr=="-"):
    print("Substraction",num1-num2)
elif (opr=="*"):
    print("Multiplication",num1*num2)
elif (opr=="/"):
    print("Division",num1/num2)
elif (opr=="%"):
    print("Remainder:",num1%num2)
else:
    print("Invalid opr.....")