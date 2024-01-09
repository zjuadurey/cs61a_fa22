### 1.6.1
def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x*x*x

def square(x):
    return x*x

def sum_cubes(n):
    return summation(n, cube)

def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))

### 1.6.2 golden ratio

def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1 / guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance

approx_phi = improve(golden_update, square_close_to_successor)
from math import sqrt

phi = 1/2 + sqrt(5)/2

def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'

improve_test()

### 1.6.3

def average(a, b):
    return (a + b) / 2

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)