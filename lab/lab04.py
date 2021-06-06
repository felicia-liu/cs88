######################
# Required Questions #
######################

# Question 4

def compose(f, g):
    """Write a function that takes in 2 single-argument functions, f and g, and returns another lambda function
    that takes in a single argument x. The returned function should return the output of applying f(g(x)).
    Hint: The staff solution is only 1 line!

    Return the composition function which given x, computes f(g(x)).

    >>> add_two = lambda x: x + 2  		# adds 2 to x
    >>> square = lambda x: x ** 2 		# squares x
    >>> a = compose(square, add_two) 	# (x + 2 ) ^ 2
    >>> a(5)
    49
    >>> mul_ten = lambda x: x * 10 		# multiplies 10 with x
    >>> b = compose(mul_ten, a) 		# ((x + 2 ) ^ 2) * 10
    >>> b(5)
    490
    >>> b(2)
    160
    """
    return lambda x: f(g(x))



# Question 5

def mul_by_num(num):
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
    return lambda x: num * x



# Required Practice Problems.
def lab04_practice_problems():
  """
  Fill in the values for these two variables.
  You will get the special code from the study tool when you complete all quesitons from lab.
  This code will be unique to your okpy email and this lab.
  Go here to practice: https://codestyle.herokuapp.com/cs88-lab04
  """
  okpy_email = "felicialiu@berkeley.edu"
  practice_result_code = "24a2550199b8654f7475e7eb911fdf7e"
  return (okpy_email, practice_result_code)
