# Tree Class
class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.entry) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def is_leaf(self):
        return not self.branches




####################
## Tree Questions ##
####################

# Q1
def tree_map(fn, t):
    """Maps the function fn over the entries of t and returns the
    result in a new tree.
    >>> numbers = Tree(1,
    ...                [Tree(2,
    ...                      [Tree(3),
    ...                       Tree(4)]),
    ...                 Tree(5,
    ...                      [Tree(6,
    ...                            [Tree(7)]),
    ...                       Tree(8)])])
    >>> print(tree_map(lambda x: 2**x, numbers))
    2
      4
        8
        16
      32
        64
          128
        256
    >>> print(numbers)
    1
      2
        3
        4
      5
        6
          7
        8
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return Tree(fn(t.entry))
    else:
        return Tree(fn(t.entry), [tree_map(fn, branch) for branch in t.branches])

# Q2
def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>> t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    def add_leaves(t, d):
        "*** YOUR CODE HERE ***"
        for branch in t.branches:
            add_leaves(branch, d + 1)
        for i in range(d):
            t.branches.append(Tree(v))
    add_leaves(t, 0)




###################################
## Iterator/Generator Questions ##
###################################

def naturals(initial=1, step=1):
    i = initial
    while True:
        yield i
        i += step

# Q3
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.start = start - 1
        self.line = self.start
        self.end = end

    def __next__(self):
        "*** YOUR CODE HERE ***"
        if self.start == self.end:
            self.start = self.line
            raise StopIteration
        else:
            self.start += 1
            return self.start

    def __iter__(self):
        "*** YOUR CODE HERE ***"
        return self



# Q4
from math import sqrt

def is_prime(n):
    """
    Return True if n is prime, false otherwise.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(19)
    True
    """
    "*** YOUR CODE HERE ***"
    divisor = 2
    if n < 2:
        return False
    while divisor <= n**0.5:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

def primes():
    """
    An infinite generator that outputs primes.

    >>> p = primes()
    >>> for i in range(3):
    ...     print(next(p))
    ...
    2
    3
    5
    """
    "*** YOUR CODE HERE ***"
    n = 0
    while True:
        if is_prime(n):
            yield n
        n += 1

# Q5
def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1 and
    make sure to remove the repeated values in both.
    You can also assume that s0 and s1 represent infinite sequences.

    >>> twos = naturals(initial = 2, step = 2)
    >>> threes = naturals(initial = 3, step = 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0), next(i1)
    "*** YOUR CODE HERE ***"
    while True:
        yield min(e0, e1)
        if e0 < e1:
            e0 = next(i0)
        elif e1 < e0:
            e1 = next(i1)
        else:
            e0, e1 = next(i0), next(i1)
