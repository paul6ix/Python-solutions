#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_sums = []
    # intialized two vairiables row and column
    row = 0
    i = 0
    # adding the contstraints
    while i < 4 and len(hourglass_sums) < 16:

        # Adding the sum at the top
        top = sum(arr[row][i:i + 3])

        # Targetting the middle
        mid = arr[row + 1][i + 1]

        # Adding the sum at the buttom
        buttom = sum(arr[row + 2][i:i + 3])
        # Summing the top middle and buttom from the arrays
        arr_total = top + mid + buttom
        # Adding the it back to the array
        hourglass_sums.append(arr_total)

        if row == 0 and i == 0:
            max_sum = arr_total
        elif arr_total > max_sum:
            max_sum = arr_total
        i += 1
        if (len(hourglass_sums) % 4 == 0):
            i = 0
            row += 1

    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
