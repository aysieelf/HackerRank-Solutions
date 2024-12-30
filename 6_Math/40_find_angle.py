"""
Task:
    ABC is a right triangle, 90° at B. Therefore, ABC = 90°.
    Point M is the midpoint of hypotenuse .

    You are given the lengths AB and BC.
    Your task is to find MBC in degrees.

Input Format:
    The first line contains the length of side AB.
    The second line contains the length of side BC.

Output Format:
    Output  in degrees.
    Note: Round the angle to the nearest integer.
"""
from math import atan, degrees

# MCB = MBC = (AB / BC) INVERSE TAN

ab = int(input())
bc = int(input())

mcb = round(degrees(atan(ab / bc)))
degree_symbol = chr(176)
print(f"{mcb}{degree_symbol}")