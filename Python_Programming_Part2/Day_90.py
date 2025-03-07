"""
Multithreding in Python
    Multithreading is a technique which allows a cpu to execute multiple threads of one process at the same time

    Thread class Functions:-
    1)run():written the thread code in run method.
    2)start():to call the run method.
    3)join():helps to run the multiple thread at the same time
    4)isAlive():It Indicates that the thread is at running state or in dead state
    5)setName():to set the Name of the thread
    6)getName():to get the Name of the thread

Thread:-
    Thread is a pre-defined class which is available in threading module
"""
#single thread  (main)
import time
class A:
    def run(self):
        for i in range(5):
            print("Akash")
            time.sleep(1)

class B:
    def run(self):
        for i in range(5):
            print("Lokesh")
            time.sleep(1)

obj=A()      #total time consumed :5 sec
obj1=B()     #total time consumed :5 sec

obj.run()
obj1.run()
 #overall time consumed by main thread :10 sec
print("-------------------------------------------")
#Multiple threading
#Here there are three threads(Ankush,Akash,Main)
import time
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print("Ankush")
            time.sleep(1)

class B(Thread):

    def run(self):
        for i in range(5):
            print("Akash")
            time.sleep(1)

t1=A()
t2=B()

t1.start()
t2.start()

t1.join()
t2.join()

print("Sunny")

