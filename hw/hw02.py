"""Homework 2."""

def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    first = 0
    second = 1
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        while n >= 1:
            ans = first + second
            first = second
            second = ans
            n -= 1
        return first


def right_triangle(a, b, c):
    """Determine whether a, b, and c can be sides of a right triangle
    >>> right_triangle(1, 1, 1)
    False
    >>> right_triangle(5, 3, 4)
    True
    >>> right_triangle(8, 10, 6)
    True
    """
    if a==b and b == c and a ==c:
        return False
    else:
        smallest = min(a, b, c)
        largest = max(a, b, c)
        middle_sq = largest**2 - smallest**2
        middle = middle_sq**(1/2)
        return middle // 1 == middle


def gets_discount(x, y):
    """ Returns True if this is a combination of a senior citizen
    and a child, False otherwise.

    >>> gets_discount(65, 12)
    True
    >>> gets_discount(9, 70)
    True
    >>> gets_discount(40, 45)
    False
    >>> gets_discount(40, 75)
    False
    >>> gets_discount(65, 13)
    False
    >>> gets_discount(7, 9)
    False
    >>> gets_discount(73, 77)
    False
    >>> gets_discount(70, 31)
    False
    >>> gets_discount(10, 25)
    False
    """
    return (x <= 12 and y >= 65) or (x >= 65 and y <= 12)


def mul_by_num(factor):
    """
    Returns a function that takes one argument and returns num
    times that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    def f(num):
        return factor * num
    return f



def count_cond(mystery_function, n):
    """
    >>> def divisible(n, i):
    ...     return n % i == 0
    >>> count_cond(divisible, 2) # 1, 2
    2
    >>> count_cond(divisible, 4) # 1, 2, 4
    3
    >>> count_cond(divisible, 12) # 1, 2, 3, 4, 6, 12
    6

    >>> def is_prime(n, i):
    ...     return count_cond(divisible, i) == 2
    >>> count_cond(is_prime, 2) # 2
    1
    >>> count_cond(is_prime, 3) # 2, 3
    2
    >>> count_cond(is_prime, 4) # 2, 3
    2
    >>> count_cond(is_prime, 5) # 2, 3, 5
    3
    >>> count_cond(is_prime, 20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    i, count = 1, 0
    while i <= n:
        if mystery_function(n, i):
            count += 1
        i += 1
    return count
