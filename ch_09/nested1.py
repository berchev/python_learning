#!/usr/bin/env python

elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]

for inner_list in elements:
    print(inner_list)

for inner_list in elements:
    for item in inner_list:
        print(item)
