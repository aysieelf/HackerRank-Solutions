"""
Task:
    You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
    Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

Input Format:
    A single line of input consisting of the string S.

Output Format:
    A single line of output consisting of the modified string.
"""
from itertools import groupby

s = input()
result = []
for key, group in groupby(s):
    result.append(f"({len(list(group))}, {key})")

print(' '.join(result))