"""
Task:
    You are given two values a and b.
    Perform integer division and print a/b.

Input Format:
    The first line contains T, the number of test cases.
    The next T lines each contain the space separated values of a and b.

Output Format:
    Print the value of a//b.
    In the case of ZeroDivisionError or ValueError, print the error code.

Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
Note:
"""
cases = int(input())
results = []
for _ in range(cases):
    try:
        a, b = map(int, input().split())
        result = a // b
        results.append(str(result))
    except (ZeroDivisionError, ValueError) as e:
        results.append(f"Error Code: {e}")

print('\n'.join(results))


