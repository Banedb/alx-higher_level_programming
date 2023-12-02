#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    check = my_list[:]
    for index, i in enumerate(my_list):
        if i % 2 == 0:
            check[index] = True
        else:
            check[index] = False
    return check
