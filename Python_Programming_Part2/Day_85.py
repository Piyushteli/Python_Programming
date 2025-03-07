"""
shutil module in python
"""
#functions in shutil module
"""
import shutil
1)shutil.copy(source,destination) : It is mainly used to copy the data from file.
2)shutil.copy2(source,destination) : It is mainly used to copy the metadata of the file
3)shutil.copytree(source,destination) : It is mainly used to copy the whole folder
4)shutil.move(source,destination) : It is mainly used to move the folder 
5)shutil.rmtree(path) :remove file from folder

creating file as zip file
shutil.make_archive("file_name","format","path")

for example
shutil.make_archive("oszip","zip","path")

to check the disk utilization
total,used,free=shutil.disk_usage("C:")
It is mainly in bytes
bytes/1024=kbs
kbs/1024=MB
mbs/1024=GB
"""
import shutil
shutil.make_archive("shutil","zip","D:\\pycharm_python_programs\\python 100 days")
print("----------------------------------------------------------------")
print(shutil.disk_usage("D:\\"))