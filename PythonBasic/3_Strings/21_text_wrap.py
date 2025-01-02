"""
Task:
    You are given a string s and width w.
    Your task is to wrap the string into a paragraph of width w.

    wrap has the following parameters:
        string string: a long string
        int max_width: the width to wrap to
    Returns:
        string: a single string with newline characters ('\n') where the breaks should be

Input Format:
    The first line contains a string, s.
    The second line contains the width, w.

What I learned:
    Discovered about textwrap.fill(string, width) -
    Python's built-in text wrapping function.
"""
import textwrap

def wrap(string, max_width):
    #     result = []
    #     while len(string) > 0:
    #         if len(string) < max_width:
    #             result.append(string)
    #             return '\n'.join(result)
    #         result.append(string[:max_width])
    #         string = string[max_width:]

    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)