"""
Rock, Paper ,Scissors game using Random Module

Winning Rules as Follows :
1)Rock vs Paper -> Paper Wins
2)Rock vs Scissors -> Rock Wins
3)Paper vs Scissors -> Scissor Wins
"""
import random
l=["Rock","Paper","Scissors"]
while True:
    c_count = 0
    u_count = 0
    uc=int(input("""
    Do you want to Start Game:-
    1)Yes
    2)No | Exit
    
    """))

    if uc==1:
        for i in range (1,6):
            user_Input=int(input("""
            Enter your Choice:
            1)Rock
            2)Paper
            3)Scissors
            
            """))
            if user_Input==1:
                u_choice="Rock"
            elif user_Input==2:
                u_choice="Paper"
            elif user_Input==3:
                u_choice="Scissors"
            C_choice=random.choice(l)


            if u_choice==C_choice:
                print("Computer choice is ", C_choice)
                print("user choice is ", u_choice)
                print("Draw Game...")
                u_count+=1
                c_count+=1

            elif (u_choice=="Paper" and C_choice=="Rock") or (u_choice=="Rock" and C_choice=="Scissors") or (u_choice=="Scissors" and C_choice=="Paper"):
                print("Computer choice is ", C_choice)
                print("user choice is ", u_choice)
                print("You win")
                u_count+=1

            else:
                print("Computer choice is ", C_choice)
                print("user choice is ", u_choice)
                print("Computer win")
                c_count += 1


        if u_count > c_count:
            print("You Win Final Game.... ")

        elif u_count < c_count:
            print("Computer Win the Final Game....")

        else:
            print("The Final Game is Draw...")


    else:
        break




