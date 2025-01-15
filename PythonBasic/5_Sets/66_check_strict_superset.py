"""
Task:
    You are given a set A and n other sets.
    Your job is to find whether set A is a strict superset of each of the N sets.
    Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
    A strict superset has at least one element that does not exist in its subset.

Input Format:
    The first line contains the space separated elements of set A.
    The second line contains integer n, the number of other sets.
    The next n lines contain the space separated elements of the other sets.
"""
a = set(input().split())
n = int(input())

result = True
for _ in range(n):
    n_set = set(input().split())
    if not (a > n_set):
        result = False
        break

print(result)