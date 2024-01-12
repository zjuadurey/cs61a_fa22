from math import sqrt, pow
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

## 1.6.4

def square(x):
    return x * x

def successor(x):
    return x + 1

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

square_successor = compose1(square, successor)

result = square_successor(12)

### 1.6.5

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

def power(x, n):
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n - 1)
    return find_zero(f, df)

### 1.6.6 curry

def curried_square(x):
    def curried_y(y):
        return x * y
    return curried_y

def curried_2_bit(bit_2):
    def curried_1_bit(bit_1):
        return bit_2 * 10 + bit_1
    return curried_1_bit

def curried_3_bit(bit_3):
    def curried_2_bit(bit_2):
        def curried_1_bit(bit_1):
            return bit_3 * 100 + bit_2 * 10 + bit_1
        return curried_1_bit

    return curried_2_bit

def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1

### use curry2
result_curry = curry2(pow)(2)(3)

### use curried_pow in map_to_range: 
def g():
    map_to_range(0, 10, curried_pow(2))

### uncurry2
def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f

### 1.6.7 lambda

def compose1(f, g):
    return lambda x : f(g(x))

f = compose1(lambda x : x * x, lambda y : y + 1)

result = f(12)

s = lambda x : x * x

compose1 = lambda f,g: lambda x: f(g(x))

### 1.6.7 decorators

def trace(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3 * x

import time

def tiktok(fn):
    def wrapper():
        t1 = time.time()
        fn()
        t2 = time.time() - t1
        print(fn.__name__, ' took', t2, ' seconds')
    return wrapper

@tiktok
def do_this():
    time.sleep(0.01)