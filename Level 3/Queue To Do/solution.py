import operator
from functools import reduce


def f(n):
    """
    Return the fast XOR of numbers from 1 to n.
    
    Based on:
    https://www.geeksforgeeks.org/calculate-xor-1-n/
    """
    modulus = n & 3  # n % 4

    if modulus == 0:
        return n

    if modulus == 1:
        return 1

    if modulus == 2:
        return n + 1

    return 0


def xor_range(a, b):
    """
    Return the XOR of numbers from A to B.
    """
    return f(b) ^ f(a - 1)


def solution(start, length):
    return reduce(
        operator.xor,
        [xor_range(start + (l * length), start + (l * length) + length - l - 1) for l in range(length)]
    )
