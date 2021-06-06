######################
# Required Questions #
######################
def f1():
    """
    >>> f1()
    3
    """
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    return lambda: 3

def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x: 3

def f4():
    """
    >>> f4()()(3)()
    3
    """
    return (lambda: lambda: lambda x: lambda: x)()


def lambda_curry2(fn):
    """
    Returns a Curried version of a two argument function func.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    return lambda x: lambda y: fn(x, y)



from operator import add, mul

def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    x = base
    for i in s:
        ans = reducer(base, i)
        x = reducer(x, ans)
    return x


from operator import add, mul

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)   # 2 * 1^2 * 2^2 * 3^2
    72
    """
    total = base
    k = 1
    while k <= n:
        total = combiner(total, term(k))
        k = k+1
    return total

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> square = lambda x: x * x
    >>> triple = lambda x: 3 * x
    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    """
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> square = lambda x: x * x
    >>> triple = lambda x: 3 * x
    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    """
    return accumulate(mul, 1, n, term)
