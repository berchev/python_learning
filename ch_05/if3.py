#!/usr/bin/env python

ph = float(input('Enter pH value: '))

if ph < 7.0:
    print(ph, 'is acidic')
elif ph > 7.0:
    print(ph, "is basic")
    