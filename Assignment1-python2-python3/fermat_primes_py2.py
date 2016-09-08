#!/usr/bin/python
import random
from newton_sqrt_py2 import newton_sqrt


def remainder(a, b):
    return a % b

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def expmod(b, e, m):
    if e == 0:
        return 1
    elif is_even(e):
        x = expmod(b, e / 2, m)
        return remainder(x*x, m)
    else:
        return remainder(b * expmod(b, e - 1, m), m)

def fermat_test(n):
    a = random.randint(1, n - 1)
    return expmod(a, n, n) == a;

def is_fermat_prime(n, num_times):
    for t in xrange(num_times + 1):
        if not fermat_test(n):
            return False
    return True

def sum_of_fermat_primes(n, num_times):
    rslt=0
    for i in xrange(2, n + 1):
        if is_fermat_prime(i, num_times):
            rslt += i
    return rslt

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for d in xrange(2, int(newton_sqrt(n)) + 1):
            if n % d == 0:
                return False
        return True

def sum_of_primes(n):
    rslt = 0
    for i in xrange(2, n + 1):
        if is_prime(i):
            rslt += i
    return rslt

def test_sum_diff_in_range(n):
    sp = sum_of_primes(n)
    sfp = sum_of_fermat_primes(n, 10)
    print 'sum of primes = ', sp
    print 'sum of fermat primes = ', sfp
    print 'sum diff = ', sfp - sp
