#!/usr/bin/env python

clegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
useful_markers = clegans_phenotypes[0:4]

print(useful_markers)

print(clegans_phenotypes[:4])
print(clegans_phenotypes[4:])

clegans_copy = clegans_phenotypes[:]
print(clegans_copy)