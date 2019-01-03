#!/usr/bin/env python
total = 0
avr = 0
for i in range(2, 23):
    total = total + i
    avr = total / len(range(2, 23))

print(total)
print(avr)

