while True:
    print(f"\n!!!Menu!!!!\n 1.)Addition \n 2)Subraction \n 3)Multiplication \n 4)Division \n 5)power \n 0)exit")

    choice = int(input("Enter the choice: "))
    if (choice == 0):
        print("Good Bye")
        break

    if choice == 1 or choice <= 5:
        a = int(input("Enter the First number: "))
        b = int(input("Enter the second number: "))

        if choice == 1:
            print(f"addition={a + b}")

        elif choice == 2:
            print(f"subtraction={a - b}")

        elif choice == 3:
            print(f"Multiplication={a * b}")

        elif choice == 4:
            print(f"Division={a / b}")
        else:
            print(f"power={a ** b}")

    else:
        print("Invalid choice")
