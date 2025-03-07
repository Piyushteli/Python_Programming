l=[]
while True:
    print(f"!!!Menu!!!\n1)push \n2)pop \n3)last \n4)Display \n5)Exit ")
    choice=(int(input("Enter the Choice: ")))
    if choice==1:
        n=input("Enter the Element: ")
        l.append(n)
        print(l)
    elif choice==2:
        if len(l)==0:
            print("Stack is Empty")
        else:
            print(l.pop())
            print(l)
    elif choice==3:
        print(l[-1])
    elif choice==4:
        print("ELEMENT OF STACK :",l)
    elif choice==5:
        break
    else:
        print("Invalid choice")
