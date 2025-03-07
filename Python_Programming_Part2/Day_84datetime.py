"""
datetime module in Python

function
1)datetime.datetime.now()
2)datetime.datetime()
3)datetime.strftime()
"""
import datetime
print(datetime.datetime.now())
print(datetime.datetime(2025,1,7))
x=datetime.datetime.now()
print(x)
print("Year",x.strftime("%Y"))
print("Year",x.strftime("%y"))
print("Month as number: ",x.strftime("%m"))
print("Minute",x.strftime("%M"))
print("Month",x.strftime("%b"))
print("Month",x.strftime("%B"))
print("Second",x.strftime("%S"))
print("Hour 00-23:",x.strftime("%H"))
print("Hour 00-12:",x.strftime("%I"))
print("AM/PM:-",x.strftime("%I %p"))

