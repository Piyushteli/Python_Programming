"""
4)Time module in Python and calender
        1)time related Functions
1)time()
2)localtime()
3)gmtime()
4)ctime
5)sleep()

        2)time formatting functions
1)strftime()
2)strptime()



"""
from time import time,ctime,localtime

t=time()           #returns time in second
print(t)

ct=ctime()
print(ct)

lt=localtime()
print(lt.tm_hour,":",lt.tm_min,":",lt.tm_sec)
print(lt.tm_mday,"/",lt.tm_mon,"/",lt.tm_year)
print(lt)
print("------------------------------------------")
import time
print("WELCOME TO COLLEGE")
time.sleep(1)
print("welcome")
print("--------------------------------------")

import calendar
print(calendar.calendar(2025,2))
print(calendar.month(2025,2))

print("--------------------------------------")
import calendar
year=int(input("Enter the year: "))
mon=int(input("Enter the month: "))
if year<=0:
    year=int(input("Warning...!Enter the correct year"))


if mon<0 or mon>12:
    mon=int(input("Warning...!Enter the correct month"))


print(calendar.month(year,mon))
