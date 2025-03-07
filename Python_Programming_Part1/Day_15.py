#Student Grade System
Marks=int(input("Enter the Marks: "))
if (Marks>90 and Marks<=100):
    print("Grade A")
elif(Marks>80 and Marks<=90):
    print("Grade B")
elif (Marks>70 and Marks<=80):
    print("Grade C ")
elif(Marks>60 and Marks<=70):
    print("Grade D")
elif(Marks>50 and Marks<=60):
    print("Grade E1")
elif(Marks>40 and Marks<=50):
    print("Grade E2")
elif (Marks<=40):
    print("Fail")
else:
    print("Invalid Input..")
