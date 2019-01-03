#!/usr/bin/env python

L1 = [1, 2, 4, 7, 8]
L2 = [4, 6, 6]

def is_longer(L1: list, L2: list) -> bool:
    return len(L1) > len(L2)

print(is_longer(L1, L2))
