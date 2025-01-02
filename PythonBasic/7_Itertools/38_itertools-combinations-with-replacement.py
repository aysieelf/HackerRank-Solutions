"""
Task:
    You are given a string S.
    Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.

Input Format:
    A single line containing the string S and integer value k separated by a space.
    The string contains only UPPERCASE characters.

Output Format:
    Print the combinations with their replacements of string S on separate lines.
"""
from itertools import combinations_with_replacement

s, k = input().split()
s = ''.join(sorted(s))

letter_combs = list(combinations_with_replacement(s, int(k)))
for comb in letter_combs:
    print(''.join(comb))
