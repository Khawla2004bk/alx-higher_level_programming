#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n = 0
    d = 0

    for tupl in my_list:
        n += tupl[0] * tupl[1]
        d += tupl[1]
    return (n / d)
