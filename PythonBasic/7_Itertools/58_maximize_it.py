"""
Task:
    You are given a function f(X) = X^2. You are also given K lists. The ith list consists of Ni elements.
    You have to pick one element from each list so that the value from the equation below is maximized:
        S = (f(X1) + f(X2) + ... + f(Xk)) % M
        X1 denotes the element picked from the ith list. Find the maximized value Smax obtained.
    Note that you need to take exactly one element from each list,
    not necessarily the largest element.
    You add the squares of the chosen elements and perform the modulo operation.
    The maximum value that you can obtain, will be the answer to the problem.

Input Format
    The first line contains 2 space separated integers K and M.
    The next K lines each contains an integer Ni, denoting the number of elements in the ith list,
    followed by Ni space separated integers denoting the elements in the list.

Output Format:
    Output a single integer denoting the value Smax.
"""
from itertools import product

K, M = map(int, input().split())
lst = []

for _ in range(K):
    row = list(map(int, input().split()))
    lst.append(row[1:])

combinations = list(product(*lst))

s_max = float('-inf')
for combination in combinations:
    temp_result = sum(map(lambda x: x**2, combination)) % M
    s_max = max(s_max, temp_result)

print(s_max)