#!/usr/bin/python
import math


def average(a, b):
    return (a + b) / 2.0

def improve_guess(trial, x):
    return average(trial, x/trial)

def is_good_enough(trial, x):
    return (abs(trial * trial - x) < 0.001)

def square_root(trial, x):
    while(not is_good_enough(trial, x)):
        trial = improve_guess(trial, x)
    return trial

def newton_sqrt(n):
    return square_root(1, n)
