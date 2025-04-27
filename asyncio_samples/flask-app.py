import requests
import asyncio
import time
from  concurrent.futures import ThreadPoolExecutor
import random
    

def call_sleep_url(seconds=3):
    sleep_url = "http://127.0.0.1:5000/sleep/{0}"
    url = sleep_url.format(seconds)
    print(url)
    response_text = requests.get(url).text
    print(response_text)    
    # Below code will also work.
    #print(f'blocking sleep {seconds}')
    #time.sleep(seconds)
    #print(f'blocking sleep end {seconds}')
    return response_text


async def call_async_sleep_url(seconds, pool=None, loop=None):
    if not loop:
        loop = asyncio.get_running_loop()        
    result = await loop.run_in_executor(pool, call_sleep_url, seconds) # await is required here.
    return result


async def main():
    seconds = [10, 3, 2, 5, 1, 1, 1, 2, 1, 2] * 10
    print(len(seconds))
    for i in range(5):
        seconds.append(random.randrange(1,5))

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        tasks = [asyncio.create_task(call_async_sleep_url(s, pool=pool, loop=loop)) for s in seconds]
        await asyncio.gather(*tasks) #await is not required here


if __name__ == '__main__':
    start_time = time.time()
    print('Starting test')

    asyncio.run(main())

    duration = time.time() - start_time
    print(f"Test completed in {duration:.2f} seconds")
