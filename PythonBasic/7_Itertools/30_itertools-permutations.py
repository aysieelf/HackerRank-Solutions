"""
Task:
    You are given a string S.
    Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format:
    A single line containing the space separated string S and the integer value k.

Output Format:
    Print the permutations of the string S on separate lines.

What I learned:
    itertools.permutations(iterable[, r])
    This tool returns successive r length permutations of elements in an iterable.
    If r is not specified or is None,
    then r defaults to the length of the iterable,
    and all possible full length permutations are generated.
    Permutations are printed in a lexicographic sorted order.
    So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
"""
import itertools

arr, k = input().split()
k = int(k)
arr = sorted(arr)
for perm in  itertools.permutations(arr, k):
    print(''.join(perm))