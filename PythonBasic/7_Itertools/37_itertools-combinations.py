"""
Task:
    You are given a string S. Your task is to print all possible combinations,
     up to size k, of the string in lexicographic sorted order.

Input Format:
    A single line containing the string S and integer value k separated by a space.
    The string contains only UPPERCASE characters.

Output Format:
    Print the different combinations of string  on separate lines.

WHAT I LEARNED:
    itertools.combinations(iterable, r) returns all possible combinations of the iterable
    I can sort the string and then use itertools.combinations to get all the combinations
"""
from itertools import combinations

s, k = input().split()
s = ''.join(sorted(s))

letter_combs = []
for i in range(1, int(k)+1):
    combs = list(combinations(s, i))
    for comb in combs:
        letter_combs.append(''.join(comb))

print('\n'.join(letter_combs))

