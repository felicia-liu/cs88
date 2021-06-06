## OOP ##

#Q1
class MixedJuiceVendor(object):
    """ A QueueVendingMachine that vends mixed juices.

    >>> vendor = MixedJuiceVendor(['kiwi', 'mango', 'apple', 'guava'], 3)
    >>> juice = vendor.dispense()
    >>> juice
    'kiwi-mango'
    >>> vendor.collect_money(juice)
    9
    >>> juice = vendor.dispense()
    >>> juice
    'apple-guava'
    >>> vendor.collect_money(juice)
    19
    >>> vendor.cups
    1
    >>> juice = vendor.dispense() # no fruits left!
    >>> print(juice)
    None

    >>> vendor2 = MixedJuiceVendor(['guava', 'mango'], 0)
    >>> juice = vendor2.dispense() # no cups!
    >>> print(juice)
    None

    >>> vendor3 = MixedJuiceVendor(['lemon'], 1)
    >>> juice = vendor3.dispense() # only one fruit!
    >>> print(juice)
    None
    """

    def __init__(self, fruits, cups):
        """ fruits is a list of fruits in the inventory. cups is the number of
            cups left to put juice in.
        """
        self.fruits = fruits
        self.cups = cups
        self.revenue = 0

    def dispense(self):
        """ Dispenses a mixed juice combining the first two fruits in the
            fruit inventory. Juices can only be created if there are at least
            two fruits left and there is at least one cup left.
        """
        "*** YOUR CODE HERE ***"
        if len(self.fruits) >= 2:
            if self.cups >= 1:
                self.cups -= 1
                return self.fruits.pop(0) + '-' + self.fruits.pop(0)


    def collect_money(self, item):
        """ Each juice is priced based on how many letters make up its two
            fruits.
        """
        "*** YOUR CODE HERE ***"
        self.revenue += len(item) - 1
        return self.revenue

#Q2
def total_revenue(qvm):
    """ Returns total possible revenue generated from qvm.

    >>> juices = MixedJuiceVendor(['orange', 'mango', 'banana', 'guava'], 10)
    >>> total_revenue(juices)
    22
    >>> more_juices = MixedJuiceVendor(['lemon', 'strawberry', 'grape', 'apple'], 20)
    >>> total_revenue(more_juices)
    25
    """
    "*** YOUR CODE HERE ***"
    if qvm.cups >= 1:
        qvm.cups -= 1
        while len(qvm.fruits) >= 2:
            item = qvm.fruits.pop(0) + '-' + qvm.fruits.pop(0)
            qvm.revenue += len(item) - 1
    return qvm.revenue
