
'''

import asyncio
async def fn():
    print('This is ')
    await asyncio.sleep(10)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')

if __name__ == '__main__':
    print(__name__)
    asyncio.run(fn()) 
'''


'''
import asyncio
 
async def fn():
    print("one")
    await asyncio.sleep(1)
    await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)
 
async def fn2():
    await asyncio.sleep(2)
    print("two")
    await asyncio.sleep(2)
    print("three")


if __name__ == '__main__':    
    asyncio.run(fn())
    
'''



import time
import asyncio
async def fn():
    task=asyncio.create_task(fn2())
    print("one")
    print('four')
    #await asyncio.sleep(1)
    time.sleep(1)
    print('five')
    #await asyncio.sleep(1)
    time.sleep(1)
 
async def fn2():
    print("two")
    #await asyncio.sleep(1)
    time.sleep(1)
    print("three")




if __name__ == '__main__':    
    asyncio.run(fn())
    
