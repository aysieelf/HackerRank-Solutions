"""
Task:
    Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format:
    The first line contains an integer N, the number of operations.
    The next N lines contains the space separated names of methods and their values.

Output Format:
    Print the space separated elements of deque d.
"""
from collections import deque

n = int(input())
d = deque([])
for _ in range(n):
    command = input()
    if command == 'pop':
        d.pop()
    elif command == 'popleft':
        d.popleft()
    else:
        command, num = command.split()
        if command == 'append':
            d.append(num)
        elif command == 'appendleft':
            d.appendleft(num)

print(' '.join(str(x) for x in d))
