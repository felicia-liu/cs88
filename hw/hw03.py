######################
# Required Questions #
######################

def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    for i in lst:
        if i != 0:
            return i


def has_n(lst, n):
    """ Returns whether or not a list contains the value n.

    >>> has_n([1, 2, 2], 2)
    True
    >>> has_n([0, 1, 2], 3)
    False
    >>> has_n([], 5)
    False
    """
    for i in lst:
        if i == n:
            return True
    return False


def deep_list(seq):
    """Returns a new list containing elements of the original list that are lists.

    >>> seq = [49, 8, 2, 1, 102]
    >>> deep_list(seq)
    []
    >>> seq = [[500], [30, 25, 24], 8, [0]]
    >>> deep_list(seq)
    [[500], [30, 25, 24], [0]]
    >>> seq = ["hello", [12, [25], 24], 8, [0]]
    >>> deep_list(seq)
    [[12, [25], 24], [0]]
    """
    return [list(i) for i in seq if type(i) is list]



def total_price(prices):
    """
    Finds the total price of all products in prices including a
    50% tax on products with a price greater than or equal to 20.
    >>> total_price([5, 20, 30, 7])
    87
    >>> total_price([8, 4, 3])
    15
    >>> total_price([10, 100, 4])
    164
    """
    return int(sum([i*1.5 if i >= 20 else i for i in prices]))


def arange(start, end, step=1):
    """
    arange behaves just like np.arange(start, end, step).
    You only need to support positive values for step.

    >>> arange(1, 3)
    [1, 2]
    >>> arange(0, 25, 2)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    >>> arange(999, 1231, 34)
    [999, 1033, 1067, 1101, 1135, 1169, 1203]

    """
    num = start
    list = []
    while num < end:
        list.append(num)
        num = num + step
    return list



def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> def fn(x):
    ...     return x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    return [[x, fn(x)] for x in seq if fn(x) >= lower and fn(x) <= upper]
