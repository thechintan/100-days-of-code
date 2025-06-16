import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print('func1')
    return "Hari"
async def function2():
    await asyncio.sleep(1)
    print('func2')
async def function3():
    await asyncio.sleep(3)
    print('func3')

async def main():
    #task = asyncio.create_task(function1())
    #await function1()
    # await function2()
    # await function3()
    L= await asyncio.gather(
        function1(),
        function2(),
        function3(),
      )
    print(L)

asyncio.run(main())