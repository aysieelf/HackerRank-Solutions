"""
Task:
    You have a non-empty set s, and you have to execute N commands given in N lines.
    The commands will be pop, remove and discard.

Input Format:
    The first line contains integer n, the number of elements in the set .
    The second line contains n space separated elements of set s.
    All the elements are non-negative integers, less than or equal to 9.
    The third line contains integer N, the number of commands.
    The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Output Format:
    Print the sum of the elements of set s on a single line.
"""
n = int(input())
s = set(map(int, input().split()))
commands = int(input())
for _ in range(commands):
    command = input()
    if command.strip() == 'pop':
        s.pop()
    else:
        command, num = command.split()
        if command == 'discard':
            s.discard(int(num))
        elif command == 'remove':
            s.remove(int(num))

print(sum(s))