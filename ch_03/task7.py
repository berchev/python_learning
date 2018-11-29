#!/usr/bin/env python

def top_three_avg(grade1, grade2, grade3, grade4):
    """

    :param grade1: number
    :param grade2: number
    :param grade3: number
    :param grade4: number
    :return: number
    """
    total = grade1 + grade2 + grade3 + grade4
    top_three = total - min(grade1, grade2, grade3, grade4)
    return top_three / 3

print(top_three_avg(20, 40, 80, 26))
print(top_three_avg(33,24,17,14))
