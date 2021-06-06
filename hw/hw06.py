######################
# Required Questions #
######################

# Probably a die-re situation

def count_change(amount, denominations):
    """Returns the number of ways to make change for amount.

    >>> denominations = [50, 25, 10, 5, 1]
    >>> count_change(7, denominations)
    2
    >>> count_change(100, denominations)
    292
    >>> denominations = [16, 8, 4, 2, 1]
    >>> count_change(7, denominations)
    6
    >>> count_change(10, denominations)
    14
    >>> count_change(20, denominations)
    60
    """
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    if len(denominations) == 0:
        return 0
    if amount > 0:
        amount = amount - denominations[0]
        return count_change(amount, denominations) + count_change(amount + denominations[0], denominations[1:])



import random
random.seed(42)

def dice(x, y):
    """Construct a die that is a list from x to y inclusive.
    >>> dice(1, 6)
    [1, 2, 3, 4, 5, 6]
    >>> dice(3, 5)
    [3, 4, 5]
    >>> dice(5, 5)
    [5]
    """
    return [i for i in range(x, y+1)]

def smallest(die):
    """Return the lowest value die can take on."""
    return min(die)

def largest(die):
    """Return the largest value die can take on."""
    return max(die)

def str_dice(die):
    """Return a string representation of die.

    >>> str_dice(dice(1, 6))
    'die takes on values from 1 to 6'
    """
    return 'die takes on values from {0} to {1}'.format(smallest(die), largest(die))

def roll_dice(die, a):
    """Roll the die a times and return an array of the rolled values.
    >>> roll_dice(dice(5, 5), 4)
    [5, 5, 5, 5]
    >>> max(roll_dice(dice(1, 6), 100))
    6
    >>> min(roll_dice(dice(1, 6), 100))
    1
    >>> x = sum(roll_dice(dice(1, 6), 1000))/1000 # Finds the mean of 1000 dice rolls
    >>> 3 <= x <= 4 # Checks if the mean is between 3 and 4
    True
   """
    result = []
    for i in range(0, a):
       result += [random.choice(die)]
    return result

def rolls_until_six(die):
    """Roll the die until you get a 6 and return the number of rolls it took to do so.
    If six is not a the possible values to roll, return a string saying '6 is not a possible value of this die'
    >>> rolls_until_six(dice(1, 5))
    '6 is not a possible value of this die'
    >>> rolls_until_six(dice(6, 6)) # Takes one roll to get 6
    1
    >>> x = sum([rolls_until_six(dice(1, 6)) for _ in range(1000)])/1000 # Repeat 1000 times and average
    >>> 5 <= x <= 7 # Check that it takes between 5 and 7 rolls overall on average
    True
    """
    no_six = '6 is not a possible value of this die'
    count = 0
    for i in die:
        count += 1
        if i == 6:
            return count
    return no_six


def cup(die_1, die_2):
    """Construct a cup that contains die1 and die2.
    >>> cup(dice(1, 1), dice(1, 2))
    [[1], [1, 2]]
    """
    return [die_1, die_2]

def add_to_cup(cup, die):
    """Add die to cup.
    >>> cup1 = cup(dice(1, 1), dice(1, 2))
    >>> add_to_cup(cup1, dice(1, 3))
    [[1], [1, 2], [1, 2, 3]]
    """
    return cup + [die]

def roll_cup(cup):
    """Roll every die in the cup and return an array of the rolled values.
    >>> roll_cup(cup(dice(1, 1), dice(2, 2)))
    [1, 2]
    """
    rolls = []
    for i in cup:
        rolls += roll_dice(i, 1)
    return rolls
