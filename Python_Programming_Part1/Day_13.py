"""
String Methods
"""
#1)upper()
str1="college"
print(str1.upper())

#2)lower()
str2="APPLE"
print(str2.lower())

#3)strip()
str3=" School Time "
print(str3.strip(" "))

#4)rstrip()
str4="Hello World...!!!"
print(str4.rstrip("!"))

#5)lstrip()
str5="!!!Hello World...!"
print(str5.lstrip("!"))

#6)replace()
str6="Silver Spoon"
print(str6.replace("Sp","M"))

#7)split()
str7="Hello World"
print(str7.split(" "))

#8)capitalize()
str8="the sun"
print(str8.capitalize())

#9)count()
str9="welcome to India"
print(str9.count("e"))

#10)center()
str10="Welcome to console..!!"
print(str10.center(30,"."))

#11)endswith()
str11="Welcome to console..!!"
print(str11.endswith("!"))

#12)find()
str12="He's name is Dan. He is an honest"
print(str12.find("is"))

str13="He's name is Dan. He is an honest"
print(str12.find("Daniel"))

#13)index()
str14="He's name is Dan. He is an honest"
print(str14.index("is"))
"""
str14="He's name is Dan. He is an honest"
print(str14.index("Daniel")) 
ValueError: substring not found
"""
#14)isalnum()
str14="English123"
print(str14.isalnum())

#15)isalpha()
str15="Math"
print(str15.isalpha())





