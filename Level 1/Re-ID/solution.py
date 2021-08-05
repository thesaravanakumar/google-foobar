import math


def solution(i):
    prm_str = concat_primes(10005)
    id = prm_str[i:i + 5]
    return id


def concat_primes(min_len):
    primes = [2, 3]
    current_len = 2
    current_num = 5
    while min_len > current_len:
        is_prime = True
        for prime in primes:
            if current_num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(current_num)
            current_len += math.ceil(math.log(current_num, 10))
        current_num += 2
    conc_prim = ""
    for prime in primes:
        conc_prim += str(prime)
    return conc_prim
