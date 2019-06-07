import time
from functools import lru_cache

@lru_cache(maxsize=4232)
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

t1=time.time()
print([fib(x) for x in range(1000)])
t2=time.time()
print(t2-t1)









# cache={}
# def doIt(num):
#     t=time.time()
#     if num in cache:
#         print('cached...')
#         return cache[num]
#     print('doing...')
#     time.sleep(2)
#     res=num*num
#     cache[num]=(res,time.time()-t)
#
#     return (res,time.time()-t)
#
# print(doIt(4))
# print(doIt(4))
# print(doIt(4))
# print(doIt(4))