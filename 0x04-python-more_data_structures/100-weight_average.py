#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weighted_sum = 0
    total_weights = 0

    for item in my_list:
        value, weight = item
        total_weighted_sum += value * weight
        total_weights += weight

    if total_weights == 0:
        return 0

    return total_weighted_sum / total_weights
