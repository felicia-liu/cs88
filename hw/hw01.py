"""Homework 1."""

def odd(number):
    """Return whether the number is odd.

    >>> odd(2)
    False
    >>> odd(5)
    True
    """
    return number%2==1


from math import sqrt

def distance(x1, y1, x2, y2):
    """Calculates the Euclidian distance between two points (x1, y1) and (x2, y2)

    >>> distance(1, 1, 1, 2)
    1.0
    >>> distance(1, 3, 1, 1)
    2.0
    >>> distance(1, 2, 3, 4)
    2.8284271247461903
    """
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def distance3d(x1, y1, z1, x2, y2, z2):
    """Calculates the 3D Euclidian distance between two points (x1, y1, z1) and
    (x2, y2, z2).

    >>> distance3d(1, 1, 1, 1, 2, 1)
    1.0
    >>> distance3d(2, 3, 5, 5, 8, 3)
    6.164414002968976
    """
    return sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)


def diff(x, y, z):
    """Return whether one argument is the difference between the other two.

    x, y, and z are all integers.

    >>> diff(5, 3, 2) # 5 - 3 is 2
    True
    >>> diff(2, 3, 5) # 5 - 3 is 2
    True
    >>> diff(2, 5, 3) # 5 - 3 is 2
    True
    >>> diff(-2, 3, 5) # 3 - 5 is -2
    True
    >>> diff(-5, -3, -2) # -5 - -2 is -3
    True
    >>> diff(-2, 3, -5) # -2 - 3 is -5
    True
    >>> diff(2, 3, -5)
    False
    >>> diff(10, 6, 4)
    True
    >>> diff(10, 6, 3)
    False


    """
    if (x - y == z):
        return True
    elif (y - x == z):
        return True
    elif (y - z == x):
        return True
    elif (z - y == x):
        return True
    elif (z - x == y):
        return True
    elif (x - z == y):
        return True
    else:
        return False



from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-5, -1)
    -4
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b) # You can replace this line, but don't have to.


from math import sqrt

def quadratic(a,b,c):
    """
    >>> quadratic(1,0,-1)
    (-1.0, 1.0)
    >>> quadratic(1,2,1)
    (-1.0, -1.0)
    >>> quadratic(1,3,-4)
    (-4.0, 1.0)
    """
    root = sqrt(b**2-4*a*c)
    return ((-b - root)/2*a, (-b + root)/2*a)


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    ans = 1
    while k > 0:
        ans = ans * (n)
        n -= 1
        k -= 1
    return ans
    if k == 0:
        ans = n
        return ans



def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
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
