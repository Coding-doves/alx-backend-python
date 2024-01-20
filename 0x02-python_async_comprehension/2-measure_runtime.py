#!/usr/bin/env python3
''' measure run time '''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' measure_runtime '''
    start = time.time()
    taks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*taks)
    end = time.time()
    return (end - start)
