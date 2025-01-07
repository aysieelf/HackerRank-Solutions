"""
Task:
    There is a horizontal row of  cubes. The length of each cube is given.
    You need to create a new vertical pile of cubes.

    When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
    Print Yes if it is possible to stack the cubes. Otherwise, print No.

Input Format:

    The first line contains a single integer T, the number of test cases.
    For each test case, there are 2 lines.
    The first line of each test case contains n, the number of cubes.
    The second line contains n space separated integers, denoting the sideLengths of each cube in that order.
"""
t = int(input())


def valid_cubes(cube: list):
    left, right = 0, len(cube) - 1
    last = float('inf')

    while left <= right:
        if cubes[left] >= cubes[right]:
            next_cube = cubes[left]
            left += 1
        else:
            next_cube = cubes[right]
            right -= 1

        if next_cube > last:
            return "No"
        last = next_cube
    return "Yes"


for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    print(valid_cubes(cubes))



