"""
Task:
    You are given two lists A and B. Your task is to compute their cartesian product AXB.

    Example:
    A = [1, 2]
    B = [3, 4]

    AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
    Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format:
    The first line contains the space separated elements of list .
    The second line contains the space separated elements of list .
    Both lists have no duplicate integer elements.

Output Format:
    Output the space separated tuples of the cartesian product.

What I learned:
    Cartesian Product (itertools.product())
    Creates all possible pairs between two sets (A×B)
"""
from itertools import product


def combinations(a, b):
    for comb in product(a, b):
        print(comb, end=' ')

a = list(map(int, input().split()))
b = list(map(int, input().split()))
combinations(a, b)