#!/usr/bin/env python

def convert_to_celsius(fahrenheit: float) -> float:
    """

    :param fahrenheit: float
    :return: float
    """
    return(fahrenheit - 32.0) * 5.0 / 9.0

print('80, 78.8, and 10.4 degrees Fahrenheint are equal to ', end='')
print(convert_to_celsius(80), end=', \n')
print(convert_to_celsius(78.8), end=', and ')
print(convert_to_celsius(10.4), end=' Celsius.\n')



