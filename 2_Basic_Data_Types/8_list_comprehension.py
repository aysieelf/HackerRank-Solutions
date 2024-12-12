"""
Task:
    You are given three integers x, y and z
    representing the dimensions of a cuboid along with an integer n.
    Print a list of all possible coordinates given by (i, j, k) on a 3D grid
    where the sum of i+j+k is not equal to n.
    Please use list comprehensions rather than multiple loops, as a learning exercise.


Input Format:
    Four integers x, y, z and n, each on a separate line.

Output Format:
    Print the list in lexicographic increasing order.
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    lst = [[ix, iy, iz] for ix in range(x+1)
           for iy in range(y+1)
           for iz in range(z+1)
           if ix + iy + iz != n]

    print(sorted(lst))
