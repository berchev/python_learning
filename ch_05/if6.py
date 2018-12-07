#!/usr/bin/env python

value = input('Enter pH value: ')

if int(value) > 0:
    ph = float(value)
    if ph < 7.0:
        print(ph, ' is acidic')
    elif ph > 7.0:
        print(ph, ' is basic')
    else:
        print(ph, ' is neutral')
else:
    print('No pH value was given!')
