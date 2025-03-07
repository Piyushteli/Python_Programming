"""
asyncio Module in Python
        Whenever we are downloading the multiple images from the internet then we mainly uses this module
"""
import time
import asyncio
import requests
async def fun1():
    URL="https://wallpapershome.com/images/pages/pic_h/5186.jpg"
    response=requests.get(URL)
    open("instagram1.jpg","wb").write(response.content)
    print("func1")
    return "HAPPY"

async def fun2():
    URL = "https://wallpapershome.com/images/pages/pic_h/5186.jpg"
    response = requests.get(URL)
    open("instagram2.jpg", "wb").write(response.content)
    print("func2")

async def fun3():
    URL = "https://wallpapershome.com/images/pages/pic_h/5186.jpg"
    response = requests.get(URL)
    open("instagram3.jpg", "wb").write(response.content)
    print("func3")

async def main():
    L=await asyncio.gather(
    fun1(),
    fun2(),
    fun3(),
    )
    print(L)
asyncio.run(main())