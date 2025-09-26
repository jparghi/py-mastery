"""Decorator examples."""

import time
from functools import wraps

def timing(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            dt = (time.perf_counter() - t0) * 1000
            print(f"{fn.__name__} took {dt:.2f} ms")
    return wrapper

@timing
def compute(n=100000):
    return sum(i*i for i in range(n))

if __name__ == "__main__":
    print(compute(200000))
