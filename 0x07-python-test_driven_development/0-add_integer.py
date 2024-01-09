#!/usr/bin/python3
"""
This module conatins the function for strictly adding 2 numbers
of data type int or floats together, any other data type is regarded
as invalid with exceptions being raise signifying what caused the error.

"""


def add_integer(a, b=98):
    """This function returns the summation of 2 numbers of data type
    int or float together

    Args:
        a: The first number
        b: The second number

    Return: a + b
    """
    data = (int, float)

    if not isinstance(a, data):
        raise TypeError("a must be an integer")
    elif not isinstance(b, data):
        raise TypeError("b must be an integer")
    edd_integer` module
===========================

Using the function `add_integer`
-------------------------------

This function adds two numbers together. The two numbers can only be any of these 2 types
1. Integer or int
2. Float

Any other data types will raise an error. Below is an example on how to use the function 
Step 1 ==> First import it
	>>> add_integer = __import__('0-add_integer').add_integer

Step 2 ==> Now use it

Below are several success and failed Test cases for the functions:

	Tests for signed and unsigned integers
	--------------------------------------
	>>> add_integer(2, 3)
	5
	>>> add_integer(-3, -7)
	-10
	>>> add_integer(-5, 8)
	3

	Tests for signed and unsigned floats
	-------------------------------------
	>>> add_integer(-2.2, -1.1)
	-3
	>>> add_integer(-1.1, 5.1)
	4

	Test for single argument
	-------------------------
	>>> add_integer(2)
	100
	>>> add_integer(-10)
	88
	>>> add_integer(6.6)
	104

	Test for more than 2 arguments
	------------------------------

	>>> add_integer(2, 3, 4)
	Traceback (most recent call last):
	TypeError: add_integer() takes from 1 to 2 positional arguments but 3 were given

	Test for wrong data type like char, str, complex, tuple, lists, dict
	-----------------------------------------------------------------------

	>>> add_integer('s', 'b')
	Traceback (most recent call last):
	TypeError: a must be an integer

	>>> add_integer((3,4), 9)
	Traceback (most recent call last):
	TypeError: a must be an integer

	>>> add_integer(4, [4,5,6])
	Traceback (most recent call last):
	TypeError: b must be an integer

	Test for infinity values
	------------------------

	>>> add_integer(float("-inf"))
	Traceback (most recent call last):
	OverflowError: cannot convert float infinity to integer

	>>> add_integer(float("inf"))
	Traceback (most recent call last):
	OverflowError: cannot convert float infinity to integer

	Test for None
	---------------------	
	
	>>> add_integer(None, None)
	Traceback (most recent call last):
	TypeError: a must be an integer
	
	Test for special NaN in python (not a number)
	>>> print(add_integer(float("NaN")))
	Traceback (most recent call last):
	ValueError: cannot convert float NaN to integerlse:
        return int(a) + int(b)
