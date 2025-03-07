"""
OS Module in python

Methods in OS module
1)os.getcwd() :-current working directory
2)os.mkdir("directory name"):It helps to create a folder
3)os.rmdir():to remove the folder
4)os.rename()
5)os.listdir()
6)os.path.exists()
7)os.chdir():change current working directory
8)os.mkdirs("directory_name"+"/directory_name): It is mainly used to create folders into the folder
9)os.getlogin(): It is used to check the user
10)os.stat().st_size: to check the size of the directory
11)os.environ["UserProfile"],"Desktop" :- To get desktop folder path
12)os.path.join(os.path.join(os.environ["UserProfile"],"Desktop"))
"""
#   Example 1
#HOW TO GET PATH OF THE FILE
import os
print(os.getcwd())
print("----------------------------")
print(os.listdir(os.getcwd()))
print("----------------------------")
print(os.path.exists(os.getcwd()))
print("----------------------------")
print(os.getlogin())
print("-----------------------------")
os.chdir("D:\\pycharm_python_programs\\python 100 days\\os_Module")
for i in range(1,10):
    os.makedirs(f"file_{i}"+"/P")

