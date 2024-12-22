"""
Task:
    You are given a complex z. Your task is to convert it to polar coordinates.

Input Format:
    A single line containing the complex number z.
    Note: complex() function can be used in python to convert the input as a complex number.

Output Format:
    Output two lines:
    The first line should contain the value of r.
    The second line should contain the value of θ.
"""
from cmath import phase

z = input()
z = complex(z)
print(abs(z))
print(phase(z))


