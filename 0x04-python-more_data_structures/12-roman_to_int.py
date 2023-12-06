#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    numerals = {
            'i': 1, 'v': 5,
            'x': 10, 'l': 50,
            'c': 100, 'd': 500,
            'm': 1000
            }
    num = 0
    prev = 0
    for n in reversed(roman_string.lower()):
        value = numerals[n]
        if value < prev:
            num -= value
        else:
            num += value
        prev = value

    return num
