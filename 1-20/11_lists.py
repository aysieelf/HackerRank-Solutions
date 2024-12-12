"""
Task:
    Initialize your list and read in the value of n
    followed by n lines of commands where each command will be of the 7 types listed above.
    Iterate through each command in order and perform the corresponding operation on your list.

Example






: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.
"""

n = int(input())

lst = []
for j in range(n):
    command = input().split()
    if "insert" in command:
        index = int(command[-2])
        integer = int(command[-1])
        lst.insert(index, integer)
    elif "print" in command:
        print(lst)
    elif "remove" in command:
        integer = int(command[-1])
        lst.remove(integer)
    elif "append" in command:
        integer = int(command[-1])
        lst.append(integer)
    elif "sort" in command:
        lst.sort()
    elif "pop" in command:
        lst.pop()
    elif "reverse" in command:
        lst.reverse()
