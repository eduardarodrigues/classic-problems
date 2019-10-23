# Eduarda Oliveira
# 2019-10-22
# the fibonacci sequence

# the fibonacci sequence is a series of numbers in which the next 
# number is found by adding up two numbers before it
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# we can define as n = (n - 1) + (n - 2), where n - 1 is the last
# number and n - 2 the second last

def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

print(fib1(5))

# the error message: maximum recursion depth exceeded.
# fib(n) calls itself with the arguments n-1 and n-2 (it's 
# recursive); you can try any n.

# avoiding recursion is our responsability. Here, the recursion
# occurs because we have not specified a base case, which is
# pretty much like a stopping point. In this case, our base cases 
# would be numbers 0 and 1, since non of them are the result of 
# the sum of two previous numbers

def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)

print(fib2(20))

# the result will be 6765. Do not try to call fib2(40); since each 
# call results in two more calls, the calls grow exponentially.
# For fib2(20), 21891 calls are made (number 20 calls numbers 19 
# and 18, and they numbers 18 and 17, and 17 and 16, respectively,
# and it goes on)

# a way out is to store the results in a python dictionary, 
# instead of calculate it every time.

# memoization is basically this: an optimization technique used 
# primarily to speed up computer programs by storing the results 
# of expensive function calls and returning the cached result when 
# the same inputs occur again

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}

# we define memo initially with the base cases

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) # here we store the results
    return memo[n]

print(fib3(50))

# now we can easily print the fiftieth position of the sequence;
# you can print(memo) to see what was storaged

# simplifying even more, we can use a built-in decorator for 
# memoizing literally any function. Since the decorator does the 
# job, we can come back to the structure of fib2()

from functools import lru_cache

@lru_cache(maxsize = None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)

print(fib4(50))

# maxsize = None means that we are not imputing any limit for
# how many of the most recent calls of the function it is 
# decorating should be cached (i.e., we are storing everything)

# iterating to find the fibonacci sequence:

def fib5(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

print(fib5(50))

# in this for loop, last is being set to the previous value of 
# next, and next is being set to the previous value of last plus 
# the previous value of next; because of that, a temporary
# variable that would hold the old value of next after last is
# updated will not be created, saving memory.

# making it more tangible: if last = 0 and next = 1, in the first 
# iteration, `last, next = 1, 0 + 1`; in the second,
# `last, next = 0 + 1, 1 + 0 + 1`, and it goes on.

# creating a generator to find the fibonacci sequence: 

from typing import Generator # Generator[YieldType, SendType, ReturnType]

def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

for i in fib6(10):
    print(i)




