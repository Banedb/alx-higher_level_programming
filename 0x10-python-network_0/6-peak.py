#!/usr/bin/python3
""" 6-peak module """


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]

    # O(1) checks for boundaries
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]

    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if list_of_integers[mid] >= list_of_integers[mid - 1]\
           and list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
