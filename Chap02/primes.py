#!/usr/bin/env python3


def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

n = 4
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')

