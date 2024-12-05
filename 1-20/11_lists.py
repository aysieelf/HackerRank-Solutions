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
