"""
Task:
    You are given a string N.
    Your task is to verify that N is a floating point number.

    In this task, a valid float number must satisfy all the following requirements:
        - Number can start with +, - or . symbol.
        - Number must contain at least 1 decimal value.
        - Number must have exactly one . symbol.
        - Number must not give any exceptions when converted using float(N).
"""
import re

n = int(input())

for _ in range(n):
    num = input()
    print(bool(re.match(r'^[+-]?\d*\.\d+$', num)))