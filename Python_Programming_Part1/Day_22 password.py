
correct_password="mypassword123"

def reset_password():
    new_password=input("Enter the new password: ")
    print("Password reset successfully....")
    return new_password

for attempt in range(5):
    user_password=input("Enter the password: ")

    if user_password==correct_password:
        print("Login Successfully...")
        break
    else:
        print(f"Incorrect password.!!!you have {4-attempt} attempt left ")

    if attempt==4:
        option=input("Forgot password ?  (yes/No)")

        if option=="yes":
            correct_password=reset_password()

        for attempt in range(5):
                user_password=input("Enter the password: ")

                if user_password==correct_password:
                    print("Login successfully")
                    break
                else:
                    print(f"Incorrect password...you have {4-attempt} attempt left")

        if attempt==4:
            print("Sorry you are locked out ")
        else:
            break
