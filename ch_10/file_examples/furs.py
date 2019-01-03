#!/usr/bin/env python

with open('hopedale.txt', 'r') as hopedale_file:
    hopedale_file.readline()
    data = hopedale_file.readline().rstrip()
    while data.startswith('#'):
        data = hopedale_file.readline().rstrip()
    print(data)

    for data in hopedale_file:
        print(data.rstrip())