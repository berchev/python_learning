#!/usr/bin/env python

#alkaline_earth_metals = [[4, 9.012], [12, 24.305],
 #                        [20, 40.078], [38, 87.62],
#                         [56, 137.327], [88, 226]]

#for i in alkaline_earth_metals:
#    print(i)

alkaline_earth_metals = [[4, 9.012], [12, 24.305],
                         [20, 40.078], [38, 87.62],
                         [56, 137.327], [88, 226]]

number_and_weight = []

for i in alkaline_earth_metals:
    number_and_weight = []
    for inner_list in alkaline_earth_metals:
        number_and_weight.append(inner_list[0])
    number_and_weight.append(inner_list[1])