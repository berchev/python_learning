#!/usr/bin/env python

t = float(input('Enter temperature: '))
source = input('Enter temperature scale (Kelvin, Celsius, Fahrenheit, Rankine, Delisle, Newton, Reaumur, Romer ): ')

def convert_temperatures(source):
    switcher={
        'Kelvin': (t - 273.15),
        'Celsius': t,
        'Fahrenheit': (t-32) * 5 / 9,
        'Rankine': (t - 491.67) * 5 / 9,
        'Delisle': 100 - t * 2 / 3,
        'Newton': t * 100 / 33,
        'Reaumur': t * 5 / 4,
        'Romer': (t - 7.5) * 40 / 21
    }
    return switcher.get(source, 'Wrong scale!')



print((convert_temperatures(source)), source)
