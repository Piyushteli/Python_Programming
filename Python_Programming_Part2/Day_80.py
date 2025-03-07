"""
Generators in Python:
    Generators in python are special type of functions that generates the values on the fly

It is mainly used to utilized the memory efficently
"""
def my_generator():
    for i in range (10):
        yield i

gen=my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(list(gen))
print("-------------------------------------")

def numbers():
    i=1
    while i<=50:
        yield i
        i=i+1

gen=numbers()
print(next(gen))
print(next(gen))
print(next(gen))
print(tuple(gen))


