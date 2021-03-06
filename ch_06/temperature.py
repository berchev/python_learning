#!/usr/bin/env python

def convert_to_celsius(fahrenheit: float) -> float:
    """
    :param fahrenheit: float
    :return: float
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0

def above_freezing(celsius: float) -> bool:
    return celsius > 0
