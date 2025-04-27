

import asyncio
import time

# This is a blocking function.
async def broken_concept_01():
    print('In broken_concept_01')
    await asyncio.sleep(3)
    print('broken_concept_01 - sleep(3) executed')
    await asyncio.sleep(1)
    print('broken_concept_01 - sleep(1) executed')

if __name__ == '__main__':
    print('broken_concept_01')
    #asyncio.run(broken_concept_01()) 



# Making the above broken_concept_01 to async
async def call_sleep(seconds):
    print(f'In call_sleep({seconds}).')
    #time.sleep(seconds)
    await asyncio.sleep(seconds)
    print(f'call_sleep({seconds}) executed')


async def async_concept_02():
    print('In async_concept_02')
    tasks = [
        asyncio.create_task(call_sleep(5)),
        asyncio.create_task(call_sleep(2)),
        asyncio.create_task(call_sleep(1))
        ]
    
    # Await Tasks Individually
    for task in tasks:
        await task
    
    # Alternative: Wait for all tasks to complete
    # await asyncio.gather(*tasks)
        

if __name__ == '__main__':
    print('async_concept_02')
    #asyncio.run(async_concept_02()) 






# Common mistake usage of asyncio
# Note: Do not use await in asyncio.create_task
'''
You are doing: await asyncio.create_task(call_sleep(x))
Immediately awaiting each task one-by-one inside the list.
🔵 This defeats the purpose of concurrency!
You are waiting for the first task to finish before even creating the second one.
This becomes sequential, not parallel/concurrent execution. 
'''

async def call_sleep(seconds):
    print(f'In call_sleep({seconds}).')
    #time.sleep(seconds)
    await asyncio.sleep(seconds)
    print(f'call_sleep({seconds}) executed')


async def async_concept_03():
    print('In async_concept_02')
    tasks = [
        await asyncio.create_task(call_sleep(5)),
        await asyncio.create_task(call_sleep(2)),
        await asyncio.create_task(call_sleep(1))
        ]

if __name__ == '__main__':
    print('async_concept_03')
    asyncio.run(async_concept_03()) 





