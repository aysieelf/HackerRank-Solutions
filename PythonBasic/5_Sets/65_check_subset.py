"""
Task:
    You are given two sets, A and B.
    Your job is to find whether set A is a subset of set B.
    If set A is a subset of set B, print True.
    If set A is not a subset of set B, print False.

Input Format:
    The first line will contain the number of test cases, T.
    The first line of each test case contains the number of elements in set A.
    The second line of each test case contains the space seperated elements of set A.
    The third line of each test case contains the number of elements in set B.
    The fourth line of each test case contains the space seperated elements of set B.

Output Format:
    Output True or False for each test case on separate lines.
"""
t = int(input())
for _ in range(t):
    len_a = int(input())
    a = set(input().split())
    len_b = int(input())
    b = set(input().split())

    print(a <= b)

