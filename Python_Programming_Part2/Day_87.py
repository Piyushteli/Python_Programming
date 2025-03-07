"""
Function catching in python   {functool module in python}
    This module is mainly use to store the cache [memoization]
    It is mainly used for limited values
"""
import functools
import time


@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(10))
print("The function runs with  value 10")

print(fx(20))
print("The function runs with  value 20")

print(fx(30))
print("The function runs with  value 30")
print("--------------------------------------------------")

print(fx(10))


print(fx(20))

print(fx(30))
print("-------------------------------------------")
print(fx(40))
print("The function runs with  value 40")

print("----------------------------------------")
import functools
@functools.lru_cache(maxsize=None)
def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(9))