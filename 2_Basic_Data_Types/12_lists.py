"""
Task:
    Initialize your list and read in the value of n
    followed by n lines of commands where each command will be of the 7 types listed above.
    Iterate through each command in order and perform the corresponding operation on your list.

Input Format:
    The first line contains an integer, n, denoting the number of commands.
    Each line  of the  subsequent lines contains one of the commands described above.

Output Format:
    For each command of type print, print the list on a new line.
"""

if __name__ == '__main__':
    N = int(input())
    lst = []

    def do_inset(args):
        lst.insert(args[0], args[1])

    def do_remove(args):
        lst.remove(args[0])

    def do_append(args):
        lst.append(args[0])

    commands_map = {
            "insert": do_inset,
            "remove": do_remove,
            "append": do_append,
            "sort": lambda _: lst.sort(),
            "pop": lambda _: lst.pop(),
            "reverse": lambda _: lst.reverse(),
            "print": lambda _: print(lst)
    }
    for _ in range(N):
        command, *args = input().split()
        args = [int(x) for x in args]
        commands_map[command](args)