#!/usr/bin/env python3
''' measure run time '''
import asyncio
import time
async_comprehension = __import__('0-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' measure_runtime '''
    start = time.time()
    await asyncio.gather(*[async_comprehension for i in range(4)])
    end = time.time()
    pause = end - start
    return pause
