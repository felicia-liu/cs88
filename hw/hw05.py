def hailstone_iterative(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_iterative(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    count = 0
    while n > 0:
        print(n)
        if n == 1:
            count += 1
            return count
        elif n % 2 == 0:
            count += 1
            n = n//2
        else:
            count += 1
            n = n*3 + 1
    return count


def hailstone_recursive(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_recursive(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        n = n//2
        return hailstone_recursive(n) + 1
    else:
        n = n*3 + 1
        return hailstone_recursive(n) + 1


def is_palindrome(lst):
    """ Returns True if the list is a palindrome. A palindrome is a list
    that reads the same forwards as backwards
    >>> is_palindrome([1, 2, 3, 4, 5])
    False
    >>> is_palindrome(["p", "a", "l", "i", "n", "d", "r", "o", "m", "e"])
    False
    >>> is_palindrome([True, False, True])
    True
    >>> is_palindrome([])
    True
    >>> is_palindrome(["a", "l", "a", "s", "k", "a"])
    False
    >>> is_palindrome(["r", "a", "d", "a", "r"])
    True
    >>> is_palindrome(["f", "o", "o", "l", "p", "r", "o", "o", "f"])
    False
    >>> is_palindrome(["a", "v", "a"])
    True
    >>> is_palindrome(["racecar", "racecar"])
    True
    >>> is_palindrome(["r", "a", "c", "e", "c", "a", "r"])
    True
    """
    if len(lst) < 3:
        return True
    elif lst[0] == lst[-1]:
        return is_palindrome(lst[1:-1])
    return False
