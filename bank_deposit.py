from datetime import datetime
import functools
from functools import singledispatch
from functools import lru_cache
import numbers


def lfu_cache(func):
    cache={}
    def wrapper(n):
        nonlocal cache
        if n in cache:
            cache[n] = cache[n] + 1
        else:
            cache = {n: 1}
        func(n)


        return cache
    return wrapper



@lfu_cache
def func(n):
    n=int(n)
    n+=1
    return n

func(2)
func(3)
func(4)
func(2)
func(6)
func(6)
print(func(4))


