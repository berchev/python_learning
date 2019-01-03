#!/usr/bin/env python
s1 = 'china'
s2 = 'czech'
ch = 'ch'

def total_occurrences(s1: str, s2: str, ch:str):

    return s1.count(ch) + s2.count(ch)


print(total_occurrences( s1, s2, ch))




