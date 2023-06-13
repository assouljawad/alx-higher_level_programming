#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_ls = []
    for i in my_list:
        if i % 2 == 0:
            new_ls.append(1)
        else:
            new_ls.append(0)
    return new_ls
