"""
Task:
    You are given a spreadsheet that contains a list of N athletes and their details
    (such as age, height, weight, and so on).
    You are required to sort the data based on the Kth attribute and print the final resulting table.
    Note that K is indexed from 0 to M-1, where M is the number of attributes.

Input Format:
    The first line contains N and M separated by a space.
    The next N lines each contain M elements.
    The last line contains K.
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    arr = sorted(arr, key=lambda x: x[k])

    for row in arr:
        print(' '.join(str(num) for num in row))
