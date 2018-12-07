#!/usr/bin/env python

population = float(input('Enter population: '))
land_area = float(input('Enter land area: '))

if population / land_area > 100:
    print('Densely populated')
