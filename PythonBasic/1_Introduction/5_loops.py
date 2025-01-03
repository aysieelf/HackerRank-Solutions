"""
Task:
    The provided code stub reads and integer, n, from STDIN.
    For all non-negative integers i < n, print i^2.

Input Format:
    The first and only line contains the integer, n.

Output Format:
    Print n lines, one corresponding to each i.
"""

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)