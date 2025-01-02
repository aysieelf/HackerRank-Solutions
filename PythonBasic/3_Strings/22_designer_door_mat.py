"""
Task:
    Mr. Vincent works in a door mat manufacturing company.
    One day, he designed a new door mat with the following specifications:

    Mat size must be NXM. ( is an odd natural number, and M is 3 times N.)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, ., - characters.
    Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
    Input Format:

    A single line containing the space separated values of N and M.

Output Format:

    Output the design pattern.
"""

def form_string(count, width):
    dot_line = '.|.'
    dash = '-'
    central_part = dot_line * count
    return central_part.center(width, dash)

if __name__ == "__main__":
    n, m = map(int, (input().split()))
    whole_str = []
    welcome = 'WELCOME'

    for i in range(1, n, 2):
        whole_str.append(form_string(i, m))

    whole_str.append(welcome.center(m, '-'))

    for i in range(n-2, 0, -2):
        whole_str.append(form_string(i, m))

    print('\n'.join(whole_str))