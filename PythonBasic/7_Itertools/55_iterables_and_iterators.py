"""
Task:
    You are given a list of N lowercase English letters.
    For a given integer K, you can select any K indices (assume 1-based indexing)
    with a uniform probability from the list.

    Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format:
    The input consists of three lines.
    The first line contains the integer N, denoting the length of the list.
    The next line consists of N space-separated lowercase English letters, denoting the elements of the list.
    The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Output Format:
    Output a single line consisting of the probability
    that at least one of the K indices selected contains the letter:'a'.

    Note: The answer must be correct up to 3 decimal places.
"""
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

all_combinations = list(combinations(letters, k))
count = sum(1 for combination in all_combinations if 'a' in combination)
print(f"{count/len(all_combinations):.3f}")