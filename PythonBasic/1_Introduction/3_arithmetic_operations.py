"""
Task
    The provided code stub reads two integers from STDIN, a and b.
    Add code to print three lines where:

    The first line contains the sum of the two numbers.
    The second line contains the difference of the two numbers (first - second).
    The third line contains the product of the two numbers.

Input Format:
    The first line contains the first integer, a.
    The second line contains the second integer, b.

Output Format:
    Print the three lines as explained above.
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    ab_sum = a + b
    ab_diff = a - b
    ab_prod = a * b

    print(ab_sum, ab_diff, ab_prod, sep='\n')