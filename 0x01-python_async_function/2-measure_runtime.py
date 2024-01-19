#!/usr/bin/env python3
''' async '''
import time


def measure_time(n: int, max_delay: int) -> float:
    ''' time it takes to spawn each '''
    start_time = time.time()
    
    # Run the wait_n coroutine and get the result
    asyncio.run(wait_n(n, max_delay))
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Return the average time per operation
    return total_time / n
