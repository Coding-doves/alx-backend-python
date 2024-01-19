#!/usr/bin/env python3
''' async '''
import asyncio
import random


async def wait_random(max_delay=10):
    ''' return random number btw 0 - 10 '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
