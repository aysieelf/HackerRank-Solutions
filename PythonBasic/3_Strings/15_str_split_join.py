"""
Task:
    You are given a string.
    Split the string on a " " (space) delimiter and join using a - hyphen.

    split_and_join has the following parameters:
        string line: a string of space-separated words
    Returns:
        string: the resulting string

Input Format:
    The one line contains a string consisting of space separated words.
"""

def split_and_join(line):
    lst = line.split()
    return "-".join(lst)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
