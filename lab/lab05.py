def sum(n):
    """Using recursion, computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    if n == 0:
        return 0
    return n + sum(n-1)


def decimal(n):
    """Return a list representing the decimal representation of a number.

    >>> decimal(55055)
    [5, 5, 0, 5, 5]
    >>> decimal(-136)
    ['-', 1, 3, 6]
    """
    #digits = [int(i) for i in str(n)]
    if n < 0:
        return ["-"] + decimal((-n)//10) + [(-n)%10]
    elif n < 10:
        return [n]
    else:
        return decimal(n//10) + [n%10]


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
       return True
    elif k == 0:
       return False
    else:
       return has_seven(k // 10)



# Practice problems (required)
def lab05_practice_problems():
  """
  Fill in the values for these two variables.
  You will get the special code from the study tool when you complete all quesitons from lab.
  This code will be unique to your okpy email and this lab.
  Go here to practice: https://codestyle.herokuapp.com/cs88-lab05
  """
  okpy_email = "felicialiu@berkeley.edu"
  practice_result_code = "581e8023d12524d430db3db47a8c53fe"
  return (okpy_email, practice_result_code)
