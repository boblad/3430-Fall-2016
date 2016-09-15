#!/usr/bin/python
from __future__ import division
from fermat_primes_py2 import expmod, fermat_test, is_prime
import math

first_34_carmichaels = [
    561,
    1105,
    1729,
    2465,
    2821,
    6601,
    8911,
    10585,
    15841,
    29341,
    41041,
    46657,
    52633,
    62745,
    63973,
    75361,
    101101,
    115921,
    126217,
    162401,
    172081,
    188461,
    252601,
    278545,
    294409,
    314821,
    334153,
    340561,
    399001,
    410041,
    449065,
    488881,
    512461,
    530881
]


def get_largest_common_divisor(numerator, denominator):
    if denominator == 0:
        return numerator
    else:
        return get_largest_common_divisor(denominator, numerator % denominator)


def is_carmichael(n):
    has_factor = False
    if n % 2 == 0:
        return False
    square_root_of_n = math.sqrt(n)
    index = 2
    while index < n:
        if index > square_root_of_n and has_factor == False:
            return False
        if get_largest_common_divisor(index, n) > 1:
            has_factor = True
        else:
            if expmod(index, n-1, n) != 1:
                return False
        index = index + 1
    return True

def find_carmichaels_in_range(x, y):
    while x <= y:
        if is_carmichael(x):
            print x
        x = x + 1

def find_first_n_carmichaels(n):
    found_carmichaels = 0
    index = 2
    while found_carmichaels < n:
        if is_carmichael(index):
            found_carmichaels = found_carmichaels + 1
            print index
        index = index + 1

def get_34_carmichaels_that_are_fermat():
    for carmichael in first_34_carmichaels:
        print fermat_test(carmichael)

def get_34_carmichaels_that_are_prime():
    for carmichael in first_34_carmichaels:
        print is_prime(carmichael)
