#!/usr/bin/env python3
""" 2-measure_runtime.py """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay) -> float:
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    totale_time = time.time() - start
    return totale_time / n
