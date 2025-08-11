##!/usr/bin/python3
""" 6-peak module """
def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return
    for idx, i in enumerate(list_of_integers[1:-1], start=1):
        if i > list_of_integers[idx - 1] and i > list_of_integers[idx + 1]:
            return i
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]
