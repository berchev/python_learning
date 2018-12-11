#!/usr/bin/env python

t = float(input('Enter temperature: '))
source = input('Enter temperature scale (Kelvin, Celsius, Fahrenheit, Rankine, Delisle, Newton, Reaumur, Romer ): ')

def convert_temperatures(t: float, source: str) -> float:
    """
    :param t: float
    :param source: str
    :return: float
    """
    if source == 'Kelvin':
        return(t - 273.15)
    elif source == 'Celsius':
        return(t)
    elif source == 'Fahrenheit':
        return((t-32) * 5 / 9)
    elif source == 'Rankine':
        return((t - 491.67) * 5 /9)
    elif source == 'Delisle':
        return(100 - t * 2 / 3)
    elif source == 'Newton':
        return(t * 100 / 33)
    elif source == 'Reaumur':
        return(t * 5 / 4)
    elif source == 'Romer':
        return((t - 7.5) * 40 / 21)
    else:
        print('Wrong temperature scale selection. Try again!')




print((convert_temperatures(t, source)), source)

