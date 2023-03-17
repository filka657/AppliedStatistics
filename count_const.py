import math


def number_of_groups(data):
    return math.ceil(1 + 3.222 * math.log10(max(data) - min(data)))


def interval_length(data, m):
    return math.ceil((max(data) - min(data)) / m)
