#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    n = 0
    for i in uniq:
        n += i
    return (n)
