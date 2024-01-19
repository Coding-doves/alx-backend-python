#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio
import random


async def wait_n(n: int, max_delay: int) -> list[float]:
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
