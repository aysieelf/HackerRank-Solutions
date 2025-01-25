"""
Task:
    You are given a space-separated list of integers.
    If all the integers are positive, then you need to check if any integer is a palindromic integer.

    Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

Input Format:
    The first line contains an integer N.
    The second line contains the N space-separated integers.
"""

n = int(input())
arr = input().split()

if all(int(num) > 0 for num in arr):
    if any(num == num[::-1] for num in arr):
        print(True)
    else:
        print(False)
else:
    print(False)