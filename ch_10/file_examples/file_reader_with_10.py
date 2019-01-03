#!/usr/bin/env python

with open('file_example.txt', 'r') as example_file:
    first_ten_chars = example_file.read(10)
    the_rest = example_file.read()
print(first_ten_chars)
print(the_rest)

