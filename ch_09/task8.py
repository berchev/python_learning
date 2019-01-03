#!/usr/bin/env python


rat_1 = [111, 112, 113, 114, 115, 116, 117, 118, 119, 120]
rat_2 = [101, 122, 117, 104, 110, 126, 137, 108, 109, 102]

if rat_1[0] > rat_2[0]:
    print("Rat 1 weighed more than rat 2 on day 1")
else:
    print("Rat 1 weighed less than rat 2 on day 1.")

if rat_1[0] > rat_2[0] and rat_1[9] > rat_2[9]:
    print("Rat 1 remained heavier than Rat 2.")
else:
    print("Rat 2 became heavier than Rat 1.")

if rat_1[0] > rat_2[0]:

    if rat_1[-1] > rat_2[-1]:
        print("Rat 1 remained heavier than Rat 2.")
    else:
        print("Rat 2 became heavier than Rat 1.")
else:
    print("Rat 2 became heavier than Rat 1.")