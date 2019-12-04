#!/usr/bin/env python3
import re
import numpy as np

start = 168630
stop = 718098
double = re.compile(r'(\d)\1')
triple = re.compile(r'(\d)\1\1')

def is_decreasing(num):
    previous = None
    for digit in str(num):
        if not previous:
            previous = digit
            continue
        if previous > digit:
            return True
        previous = digit
    return False
v_is_decreasing = np.vectorize(is_decreasing)

def has_doubles(num):
    return bool(double.search(str(num)))
v_has_doubles = np.vectorize(has_doubles)

def remove_triples(num):
    num = str(num)
    dbs = set(double.findall(num))
    tps = set(triple.findall(num))
    if dbs - tps:
        return int(num)
    else:
        return False
v_remove_triples = np.vectorize(remove_triples)

data = np.arange(start, stop)           # Create the initial data set
data = data[~v_is_decreasing(data)]     # Remove the items containing decreasing sequences
data = data[v_has_doubles(data)]        # Remove the items not containing doubles
print(f'Part 1: {len(data)}')

data = data[v_remove_triples(data)]     # Remove the items containing triplets without doubles
print(f'Part 2: {len(data)}')
