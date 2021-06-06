#############
# Iterators #
#############

# Q2
class Str:
    "*** YOUR CODE HERE ***"
    def __init__(self):
        self.string = string
        self.index = 0

    def __next__(self):
        if self.index < len(self.string):
            index = self.index
            self.index += 1
            return self.string[index]
        else:
            raise StopIteration

    def __iter__(self):
        return self


##############
# Generators #
##############

# Q3
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    i = n + 1
    while i > 0:
        yield i - 1
        i -= 1

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        while self.n > -1:
            yield self.n
            self.n -= 1



##############
#   Trees    #
##############

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



# Q4
def search(t, value):
    """Searches for and returns the Tree whose entry is equal to value if
    it exists and None if it does not. Assume unique entries.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> search(t, 10)
    >>> search(t, 5)
    Tree(5)
    >>> search(t, 1)
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    if t.entry == value:
        return t
    for branch in t.branches:
        return search(branch, value)
    return None



# Q5
def cumulative_sum(t):
    """Return a new Tree, where each entry is the sum of all entries in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return Tree(t.entry)
    else:
        entry = t.entry
        for branch in t.branches:
            entry += cumulative_sum(branch).entry
        return Tree(entry, [cumulative_sum(branch) for branch in t.branches])
