#!/usr/bin/python3
"""
    function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    size = len(list_of_integers)
    if list_of_integers is None or size == 0:
        return None

    if size == 1:
        return list_of_integers[0]

    left, right = 0, size - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
