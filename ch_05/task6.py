#!/usr/bin/env python
a = int(input('Enter digit value: '))
b = int(input('Enter digit value: '))

def different(a:int, b:int) ->bool:
    """
    :param a: int
    :param b: int
    :return: bool
    """
    return a != b

print(different(a,b))
