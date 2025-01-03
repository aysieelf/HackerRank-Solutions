"""
Task:
    You are given a string S. Your task is to find out whether S is a valid regex or not.

Input Format:
    The first line contains integer T, the number of test cases.
    The next  lines contains the string S.

Output Format:
    Print "True" or "False" for each test case without quotes.
"""
import re

n = int(input())

result = []
for _ in range(n):
    s = input()
    try:
        re.compile(s)
        result.append("True")
    except:
        result.append("False")

print('\n'.join(result))