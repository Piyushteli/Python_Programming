"""
Create a python program capable of greeting you with Good Morning,Good Afternoon and Good Evening.
Your Program should use time module to get the current hour.
"""
import time
t=time.strftime("%H:%M:%S")
hour=int(time.strftime("%H"))
hour=int(input("Enter Hour: "))
print(hour)

if hour>=0 and hour<12:
    print("Good Morning...!")

elif hour>=12 and hour<17:
    print("Good Afternoon Sir...!")

elif hour>=17 and hour<21:
    print("Good Evening Sir...!")

elif hour>=21 and hour<24:
    print("Good Night Sir...!")

else:
    print("Invalid Input...")