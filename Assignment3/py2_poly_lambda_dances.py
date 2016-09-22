#!/usr/bin/python

from datetime import datetime
import random

def make_2nd_degree_poly(k2, k1, k0):
    return lambda x: ('p(x) = {}x^2+{}x+{}'.format(k2, k1, k0),
                     (k2 * (x * x)) + (k1 * x) + k0,
                     'at x = {}'.format(x))

def make_2nd_deg_polys(coeffs):
    return [make_2nd_degree_poly(k2, k1, k0) for k2, k1, k0 in coeffs]

def map_polys(pol, numbers):
    poly_maps = []
    if type(numbers) is int:
        numbers = [numbers]
    return[poly(i) for i in numbers for poly in pol]


def display_poly_maps(poly_maps):
    for poly in poly_maps:
        print poly

def poly_dance(coeffs, xvals):
    polys = make_2nd_deg_polys(coeffs)
    poly_maps = map_polys(polys, xvals)
    return poly_maps

def gen_rand_coeff(a, b):
    sign = random.randint(1, 1000)
    if sign < 500:
        return -random.randint(a, b)
    else:
        return random.randint(a, b)

def get_nth_poly_rands(n, a, b):
    return [gen_rand_coeff(a, b) for i in xrange(0, n + 1)]

def get_nth_deg_string(n, nth_rand_polys):
    nth_deg_string = ''
    for poly in nth_rand_polys:
        if n != 0:
            nth_deg_string = nth_deg_string + str(poly) + 'x^' + str(n) + '+'
        else:
            nth_deg_string = nth_deg_string + str(poly)
        n = n - 1
    return nth_deg_string

def compute_nth_poly(x, n, nth_rand_polys):
    result = 0
    for poly in nth_rand_polys:
        if n != 0:
            result = result + (poly * (x ** n))
        else:
            result = result + poly
        n = n - 1
    return result


def make_nth_deg_rand_poly(n, a, b):
    nth_rand_polys = get_nth_poly_rands(n, a, b)
    return lambda x: ('p(x) = {}'.format(get_nth_deg_string(n, nth_rand_polys)),
                        compute_nth_poly(x, n, nth_rand_polys),
                         'at x = {}'.format(x))

def make_nth_deg_rand_polys(num_polys, n, a, b):
    return [make_nth_deg_rand_poly(n, a, b) for i in xrange(0, num_polys)]

def rand_poly_dance(num_polys, n, a, b, xvals):
    polys = make_nth_deg_rand_polys(num_polys, n, a, b)
    poly_maps = map_polys(polys, xvals)
    return poly_maps

def get_key(item):
    return item[1]

def sorted_rand_poly_dance(num_polys, n, a, b, xval):
    return sorted(rand_poly_dance(num_polys, n, a, b, xval), key=get_key, reverse=True)

def print_sorted_and_time():
    start = datetime.now()
    top_10 = sorted_rand_poly_dance(1000000, 5, 1, 10, 2)[:10]
    end = datetime.now()
    print 'start = ', start
    print'end =',end
    print 'duration = ', end - start
    display_poly_maps(top_10)
