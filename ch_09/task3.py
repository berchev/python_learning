#!/usr/bin/env python

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
print(whales)
new_whales = whales

for i in range(len(whales)):
    new_whales[i] = whales[i] + 1


print(new_whales)