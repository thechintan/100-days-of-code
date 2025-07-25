# import functools
# import time
# @functools.lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(3)
#     return n*5
# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")

#OR
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6\n")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for '6'")
print(fx(61))
print("done for '61'")