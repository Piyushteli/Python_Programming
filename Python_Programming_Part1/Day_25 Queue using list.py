l=[]
while True:
    print(f"!!!Menu!!!\n1)Enque \n2)Deque \n3)front \n4)Rear \n5)Display\n6)Exist ")
    choice=(int(input("Enter the Choice: ")))
    if choice==1:
        n=input("Enter the Element: ")
        l.append(n)
        print(l)
    elif choice==2:
        if len(l)==0:
            print("Queue is Empty")
        else:
            del l[0]
            print(l)
    elif choice==3:
        if len(l)==0:
            print("Queue is Empty")
        else:
            print(l[0])
    elif choice==4:
        if len(l) == 0:
            print("Queue is Empty")
        else:
            print(l[-1])
    elif choice==5:
        print("ELEMENT OF Queue:",l)
    elif choice==6:
        break
    else:
        print("Invalid choice")
