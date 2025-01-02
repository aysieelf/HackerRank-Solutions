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

What I learned:
   from cmath import phase
   This tool/function comes from the cmath module (complex math) and helps us calculate the angle (phase/argument) of a complex number.

   abs(complex_number) and phase(complex_number)
   These functions convert Cartesian coordinates (x,y) to Polar coordinates (r,θ):
       - abs(): Calculates the distance (r) from the point to origin (0,0)
       - phase(): Calculates the angle (θ) from positive x-axis counter-clockwise

   complex(input_string)
   This function converts a string input into a complex number that Python can work with.
   For example:
       - Input: "1+1j"
       - Becomes: complex number with real part 1 and imaginary part 1
"""
from cmath import phase

z = input()
z = complex(z)
print(abs(z))
print(phase(z))


