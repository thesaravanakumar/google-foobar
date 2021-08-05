import math


def solution(total_lambs):
    return max_henchmen(total_lambs) - min_henchmen(total_lambs)


# stingy (fibonacci)
def max_henchmen(total_lambs):
    golden_ratio = (1+5**0.5)/2
    n = 0
    curr_number = 0
    while curr_number < total_lambs:
        n += 1
        curr_number = (golden_ratio**n - (-golden_ratio)**(-n))/(2*golden_ratio-1)
    return n - 2


# generous x^2 - 1
def min_henchmen(total_lambs):
    return math.floor((total_lambs + 1) ** 0.5)
    