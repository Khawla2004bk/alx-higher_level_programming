#!/usr/bin/python3
'''Defines a Pascal's triangle function'''


def pascal_triangle(n):
    '''Represent Pascal's Triangle'''
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        prev = triangle[-1]
        nxt = [1]
        for i in range(len(prev) - 1):
            nxt.append(prev[i] + prev[i + 1])
        nxt.append(1)
        triangle.append(nxt)
    return triangle
