#!/usr/bin/env python
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']

def remove_last_item(L: list) -> list:
    del L[-1]
    return L

print(remove_last_item(celegans_phenotypes))

