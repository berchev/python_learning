#!/usr/bin/env python

half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]
print(len(half_lives))
print(max(half_lives))
print(min(half_lives))
print(sum(half_lives))
print(sorted(half_lives))

original = ['H', 'He', 'Li']
final = original + ['Be']
print(final)

metals = ['Fe', 'Ni']
print(metals * 3)

del metals[0]
