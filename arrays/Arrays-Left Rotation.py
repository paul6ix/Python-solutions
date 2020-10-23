#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    #iterating for the number of rotations
    for i in range(d):
    #Assigning the first number in the array

        temp_variable = a[0]
    #Deleting the first number in array
        a.pop(0)
    #addiing the number back in the arrary
        a.append(temp_variable)
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
