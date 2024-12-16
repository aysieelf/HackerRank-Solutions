"""
Task:
    You are asked to ensure that the first and last names of people
    begin with a capital letter in their passports.
    For example, alison heck should be capitalised correctly as Alison Heck.

    Given a full name, your task is to capitalize the name appropriately.

Input Format:
    A single line of input containing the full name, S.

Output Format:
    Print the capitalized string, S.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.capitalize()
    res = [s[0]]
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            if s[i].isalpha():
                res.append(s[i].upper())
                continue

        res.append(s[i])

    return ''.join(res)

if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)
