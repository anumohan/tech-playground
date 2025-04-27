

# 🔥 01. Simple: dealing with blocking function
# Here time.sleep() is the blocking function
# -----------------------------------------------

import time
import asyncio

async def async_sleep(seconds):
    loop = asyncio.get_running_loop()
    print(f'sleeping {seconds} seconds.')    
    await loop.run_in_executor(None, time.sleep, seconds)
    print(f'end {seconds} seconds.')

async def O1_main_sleep():
    print('stat main_sleep')
    tasks = [
        asyncio.create_task(async_sleep(5)),
        asyncio.create_task(async_sleep(2)),
        asyncio.create_task(async_sleep(1))
        ]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    print('end main_sleep')




# 🔥 02. Simple: dealing with blocking function
# Here call_sleep_url is the non async function and
# requests.get() methos is the blocking function
# ----------------------------------------------------

import requests
import asyncio
from  concurrent.futures import ThreadPoolExecutor


def call_sleep_url(seconds=3):
    sleep_url = "http://127.0.0.1:5000/sleep/{0}"
    url = sleep_url.format(seconds)
    print(url)
    response_text = requests.get(url).text
    print(response_text)
    return response_text


async def call_async_sleep_url(loop2, seconds):
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, call_sleep_url, seconds) # await is required here.
        return result


async def O2_main_call_requests_sleep():
    seconds = [10, 3, 2, 5, 1, 1, 1]
    tasks = [asyncio.create_task(call_async_sleep_url(None, s)) for s in seconds]
    await asyncio.gather(*tasks) #await is not required here
    



if __name__ == '__main__':    
    #asyncio.run(O1_main_sleep())
    asyncio.run(O2_main_call_requests_sleep())

