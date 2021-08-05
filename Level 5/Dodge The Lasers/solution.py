"""
    Problem
    =======

    For every number i in range 1 to n, return the sum of the integer portions
    of the equation i * sqrt(2).

        S(n) = floor(sqrt(2)) + ... + floor(n * sqrt(2))

    Example:

        S(3) = floor(sqrt(2)) + floor(2 * sqrt(2)) + floor(3 * sqrt(2))

             = 1 + 2 + 4
               
             = 7

    As numbers can be as large as 10^100 an iterative approach will not work.

    References
    ==========

    https://en.wikipedia.org/wiki/Beatty_sequence
    http://mathworld.wolfram.com/BeattySequence.html
    https://mathbitsnotebook.com/Algebra2/Sequences/SSGauss.html
    https://www.wolframalpha.com

    Beatty Sequences
    ================

    "Sometimes, it's easier to take a step back and concentrate not on what you
     have in front of you, but on what you don't."

    This phrase is actually a surprising help in solving this particular
    problem as it points us towards Beatty sequences (at least I felt it did).

    A Beatty sequence (see references) is defined as the sequence of integers
    found by taking the floor of the positive multiples of a positive
    irrational number.

    A positive irrational number r generates the Beatty sequence:

        Br = |_r_|, |_2r_|, |_3r_|, ..., where |_x_| is the floor function

    If r > 1, then s = r / (r - 1) is also a positive irrational number.

    These two numbers satisfy the equation 1 / r + 1 / s = 1.

    The two Beatty sequences these numbers generate are:

        Br = (|_nr_|) for n >= 1 and

        Bs = (|_ns_|) for n >= 1

    These two sequences are complimentary, meaning that together they contain
    every positive integer without repetition. In other words, every positive
    integer belongs to exactly one of these two sequences.

    Therefore:

        (|_nr_|) and (|_ns_|) for n >= 1 partition N

    As a matter of interest, OEIS provide numerous mathematical sequences, two
    of which are of particular relevance to us:

        Parameter       OEIS      Series
        ---------------------------------------------------------------
        a = sqrt(2)      A001951  1, 2, 4, 5, 7, 8, 9, 11, 12, ...
        b = 2 + sqrt(2)  A001952  3, 6, 10, 13, 17, 20, 23, 27, 30, ...

    Gauss Formula
    =============

    Gauss's formula defines the sum, Sn of n terms of an arithmetic series, as:

        Sn = n * (a1 + an) / 2, where n is the number of terms and a1 and an are
                                the first and last terms of the sequence
    
    Solution
    ========

    Using the definition of Beatty sequences above, we know that:

    If r = sqrt(2), then:
    
        r > 1 is true                       (see above)
    
    Therefore:

        s = r / (r - 1)                     (see above)
    
          = sqrt(2) / (sqrt(2) - 1)
        
          = 2 + sqrt(2)
        
    We also know that:

        (|_nr_|) and (|_ns_|) for n >= 1 partition N

    Therefore:

        (|_nr_|) = N - (|_ns_|)

    So, if we let m = floor(n * r), then:

        S(r, n) = m * (m + 1) / 2 - S(s, floor(m / s))

    While the equation produces the correct results, it still only passes 3/10
    tests, which we'll assume is down to the recursion depth and/or the
    precision.

    To tackle the precision we'll try using Decimal instead of float and adjust
    the precision of the decimal module accordingly.

    Next, we'll look at the simplifying the equation some more and specifically
    try to find a way to increase the step sizes, in order to reduce the number
    of recursions required.

    So, if we let n' = floor(m / s), then:

        n' = floor(m / s)

           = floor(m / (r / (r - 1))        (see above)
           
           = floor(m * (r - 1) / r)
           
           = floor((m * r - m)) / r)
           
           = floor(m - m / r)

    And, we also know s = 2 + sqrt(2), so:

        S(s, n) = S(2 + sqrt(2), n')

                = S(2, n') + (sqrt(2), n')

    So, simplifying with gauss's formula, we get:

        S(s, n) = n' * (n' + 1) + (sqrt(2), n')

    Therefore, our equation is now looking like:

        m = floor(n * r)

        n' = (m - (m / r))

        S(r, n) = m * (m + 1) / 2 - n' * (n' + 1) - S(r, n')

    TODO:
    m and n' can be simplified further, but the equation works successfully as
    is and manages to pass all tests.
"""

from decimal import Decimal, getcontext

getcontext().prec = 101  # Allow for at least 100 digits

SQRT2 = Decimal(2).sqrt()  # Use decimal for better precision


def beatty(n, r=SQRT2):
    """
    Return the sum of the integer portions of i * r for all numbers in the
    range 1..n inclusive.
    """

    if n < 1:
        return 0

    # Calculate m and n'
    m = int(n * r)
    n_prime = int(m - (m / r))

    # m * (m + 1) / 2 - S(s, n')
    return (
        m * (m + 1) // 2
        - n_prime * (n_prime + 1)
        - beatty(n_prime, r)  # Recurse from n'
    )


def solution(str_n):
    n = int(str_n)

    # Initial bounds check
    if n < 1 or n > 10**100:
        return str(0)

    # Special case for n = 1
    if n == 1:
        return str(1)

    # Return the sum of the Beatty sequence S(sqrt(2), n)
    return str(beatty(n, SQRT2))
