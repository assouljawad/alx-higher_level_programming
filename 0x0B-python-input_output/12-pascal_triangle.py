#!/usr/bin/python3
""" function"""


def pascal_triangle(n):
    """returns a list of lists of integers """
    ls = []
    for i in range(n):
        ls.append([])
        for j in range(i+1):
            try:
                if j - 1 != -1:
                    ls[i].append(ls[i-1][j-1] + ls[i-1][j])
                else:
                    ls[i].append(1)
            except IndexError:
                ls[i].append(1)
    return (ls)
