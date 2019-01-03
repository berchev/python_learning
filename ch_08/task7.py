#!/usr/bin/env python

L = [4, 5, 7, 19, 4]

def same_first_last(L :list) -> bool:
    if L[0] == L[-1]:
        return True

print(same_first_last(L))
