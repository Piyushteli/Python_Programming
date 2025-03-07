"""
Multiprocessing in Python
    Multiprocessing refers to the ability of a system to support more than one processor at the same time.
"""
import multiprocessing

def print_cube(num):
    print(f"cube:{num*num*num}")

def print_square(num):
    print(f"Square:{num*num}")

if __name__=="__main__":
    p1=multiprocessing.Process(target=print_square,args=(10,))
    p2=multiprocessing.Process(target=print_cube,args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")

