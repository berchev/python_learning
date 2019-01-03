#!/usr/bin/env python

nobles = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']

gas = input('Enter a gas: ')

if gas in nobles:
    print('{} is noble.'.format(gas))
