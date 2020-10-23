#!/bin/python3

import math
import os
import random
import re
import sys

def getMaxUsingPrefixSum(arr):
    length = len(arr)
    summation = maximum = 0
    for i in range(length):
        summation += arr[i]
        maximum = max(summation,maximum)
    return maximum

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n+2)
    for query in queries:
        a, b, k = query[0], query[1], query[2]
        arr[a] += k
        arr[b+1] -= k
    return getMaxUsingPrefixSum(arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
