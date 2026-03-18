def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    Examples:
    >>> multiply(2, 3)
    6
    >>> multiply(-1, 5)
    -5
    """
    return a * b

run from terminal
====
python -m doctest src/math_tool.py -v 

output
=======
Trying:
    multiply(2, 3)
Expecting:
    6
ok
Trying:
    multiply(-1, 5)
Expecting:
    -5
ok
1 item had no tests:
    math_tool
1 item passed all tests:
   2 tests in math_tool.multiply
2 tests in 2 items.
2 passed.
Test passed.
