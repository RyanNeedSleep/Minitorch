"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x: float, y: float):
    return x * y

def add(x: float, y: float):
    return x + y

def neg(x: float):
    return -1*x

def max(x: float, y: float):
    return x if x > y else y

def inv(x: float):
    return 1/x

def id(x: float):
    return x

def is_close(x: float, y: float):
    return abs(x - y) < 1e-2

def lt(x: float, y: float):
    return x < y

def eq(x: float, y: float): 
    return x == y

def sigmoid(x: float):
    return 1 / (1 + math.exp(-x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))

def relu(x: float):
    return x if x > 0 else 0

def log(x: float):
    return math.log(x)

def exp(x: float):
    return math.exp(x)

def inv(x: float): 
    if x == 0:
        raise ZeroDivisionError("division by 0.")
    if abs(x) < 1e-300:
        return math.inf if x > 0 else -math.inf

    return 1.0 / x

def log_back(x: float, b: float):
    return b * inv(x)

def inv_back(x: float, b: float):
    return -b * 1 / (x * x)

def relu_back(x: float, b: float):
    return b if x > 0 else 0.0




# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(func: Callable):
    return lambda ls : [func(x) for x in ls] 


def zipWith(func: Callable): 
    return lambda x, y : ( func(a, b) for a, b in zip(x, y) ) 

def reduce(func, start): 
    def _reduce(func, ls, start): 
        for x in ls: 
            start = func(start, x)
        return start

    return lambda ls: _reduce(func, ls, start)


def negList(ls):
    return map(neg)(ls)

def addLists(l1, l2):
    return zipWith(add)(l1, l2)

def sum(ls):
    return reduce(add, 0.0)(ls)

def prod(ls):
    return reduce(mul, 1.0)(ls)










