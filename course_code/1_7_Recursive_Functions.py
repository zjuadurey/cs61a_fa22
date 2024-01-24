def sum_digits(n):
    if n // 10 == 0:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return last + sum_digits(all_but_last)


def fact_iter(n):
    if n == 1:
        return 1
    return n * fact_iter(n - 1)

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)

def is_even_single_recursive_version(n):
    if n == 0:
        return True
    elif n - 1 == 0:
        return False
    else:
        return is_even_single_recursive_version((n - 1) - 1)
    

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        return play_bob(n - 1)
    
def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif n % 2 == 0:
        return play_alice(n - 2)
    else:
        return play_alice(n - 1)
    

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    return count_partitions(n - m, m) + count_partitions(n, m - 1)