#!/usr/bin/env python

ids = [4353, 2314, 2956, 3382, 9362, 3900]
print(ids)

ids.remove(3382)
print(ids)


ids = [4353, 2314, 2956, 3382, 9362, 3900]
print(ids)

print(ids.index(9362))

ids.insert(5, 4499)
print(ids)

ids.extend([5566, 1830])

print(ids)

ids.reverse()
print(ids)

ids.sort()
print(ids)
