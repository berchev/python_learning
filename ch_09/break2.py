#!/usr/bin/env python

s = 'C3H7'
digit_index = -1
for i in range(len(s)):
    if s[i].isdigit():
        digit_index = i
        break
print(digit_index)