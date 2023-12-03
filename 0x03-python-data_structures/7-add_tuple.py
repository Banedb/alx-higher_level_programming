#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1, list2 = list(tuple_a[:2]), list(tuple_b[:2])
    for lst in [list1, list2]:
        while len(lst) < 2:
            lst.append(0)
    return (list1[0] + list2[0], list1[1] + list2[1])
