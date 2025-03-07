"""
re Module in Python (regular Expression in Python)
        This module is mainly used to find the pattern from the data

re module fuction
1)re.match() :It is mainly used to find the string at the beginning
2)re.search() :It is mainly used to find the string at the anywhere
3)re.split()
4)re.findall()
5)re.finditer()
6)re.sub()

characters
1)\d:-Matches any digit equivalent to [0-9]
2)\D:-Matches any non digit character
3)\W:-Matches any non-alphanumeric(only symbols) character
4)\s:-Matches any whitespaces character (space,tab,newline)

Special characters
1)^(caret) :Matches the start of a string
2)$(dollar):Matches the end of a string

"""
#Example for email validation
import re
email=input("Enter the Email:")
pattern=r'^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

if re.search(pattern,email):
    print("Email is Valid")
else:
    print("Email is invalid")
print("----------------------")
import re
text="123abc"
result=re.match(r'\d+',text)
if result:
    print(result.group())
print("---------------------------------")
import re
text="123dfg234kjl"
result=re.split(r'\d+',text)
print(result)
print("--------------------------")
import re
text="abc123"
result=re.match(r'\D+',text)
if result:
    print(result.group())
print("--------------------------------")
#searching for a pattern in re using re.search() Method
import re
pattern=r"!"           #Here the r is used to raw string
text="Hello,World!"

match=re.search(pattern,text)
if match:
    print("Match Found!")
else:
    print("Match Not Found")
print("-----------------------------------")

#searching for a pattern in re using re.findall() Method
import re
pattern=r"[A-Z]+yclone"
text="""Cyclone Domazile was a strong tropical cyclone in the
south west Indian Ocean that affected Madagascar and Reunion in
early March 2018.Dumazile originated from cyclone Dyclone low pressure area that formed near Agalega on
27 February. It became a tropical disturbance on 2 March,and was named the
next day after attaining tropical storm status Dumazile reached its peak
intensity on 5 March """

match=re.findall(pattern,text)
print(match)
print("----------------------------------------------")
#Replacing pattern using re.sub()
import re
pattern=r"[a-z]+at"
text="The cat is in the hat."
matches=re.findall(pattern,text)
print(matches)

new_text=re.sub(pattern,"dog",text)
print(new_text)