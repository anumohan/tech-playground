

import time
import asyncio
async def call_sleep(seconds):
    print(f'sleeping {seconds} seconds.')
    #time.sleep(seconds)
    await asyncio.sleep(seconds)
    print(f'end {seconds} seconds.')

async def main_sleep():
    print('stat main_sleep')
    tasks = [
        asyncio.create_task(call_sleep(5)),
        asyncio.create_task(call_sleep(2)),
        asyncio.create_task(call_sleep(1))
        ]
    

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)


    # Alternative: Await Tasks Individually
    #for task in tasks:
    #    await task

    print('end main_sleep')


if __name__ == '__main__':    
    asyncio.run(main_sleep())

