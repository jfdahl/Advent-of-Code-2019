#!/usr/bin/env python3

#############
# Setup
#############
import re
# Get the input
data = '168630-718098'
start, stop = data.split('-')
start = int(start)
stop = int(stop)

#############
# Part 1: 1686
#############
def part1(data):
    result = []

    for num in range(start, stop+1):
        dup_digit = False
        dec_digit = False
        for index, digit in enumerate(str(num)):
            if index == 0:
                previous = digit
                continue
            if previous == digit:
                dup_digit = True
            if previous > digit:
                dec_digit = True
            previous = digit
        if dup_digit and not dec_digit:
            result.append(num)

    return result

answer1 = part1(data)
print(len(answer1))


#############
# Part 2: 1145
#############
def part2(start, stop):
    results = []
    dup = re.compile(r'(\d)\1')
    trip = re.compile(r'(\d)\1\1')

    def is_decreasing(num):
        previous = []
        for digit in num:
            if not previous:
                previous.append(digit)
                continue
            if previous[-1] > digit:
                return True
            previous.append(digit)
        return False
            

    def check_number(num):
        if is_decreasing(num):
            return

        trips = trip.findall(num)
        dups = dup.findall(num)
        if set(dups) - set(trips):
            return num


    for num in range(start, stop+1): #[112233, 123444, 111122, 123436, 11122333]: #
        result = check_number(str(num))
        if result:
            results.append(result)

    return results

answer2 = part2(start, stop)
print(len(answer2))
