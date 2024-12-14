"""
Task:
    Given an integer, n, print the following values for each integer i from 1 to n:
        Decimal
        Octal
        Hexadecimal (capitalized)
        Binary

    print_formatted has the following parameters:
        int number: the maximum value to print
    Prints:
    The four values must be printed on a single line in the order specified above for each i from 1 to n.
    Each value should be space-padded to match the width of the binary value of number
    and the values should be separated by a single space.

Input Format

A single integer denoting n.
"""

def print_formatted(number):
    width = len(str(bin(number))[2:])

    result = []
    for i in range(1, number+1):
        octal = str(oct(i))[2:]
        hexadecimal = str(hex(i))[2:].upper()
        binary = str(bin(i))[2:]

        result.append(f"{str(i).rjust(width)} {octal.rjust(width)} "
                      f"{hexadecimal.rjust(width)} {binary.rjust(width)}")

    print('\n'.join(result))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)