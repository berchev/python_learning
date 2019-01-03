#!/usr/bin/env python

s = 'C3H7'
digit_index = -1
for i in range(len(s)):
    if digit_index == -1 and s[i].isdigit():
        digit_index = i
print(digit_index)