"""
Task:
    Given an integer, n, perform the following conditional actions:

    If n is odd, print Weird
    If n is even and in the inclusive range of 2 to 5, print Not Weird
    If n is even and in the inclusive range of 6 to 20, print Weird
    If n is even and greater than 20, print Not Weird

Input Format:
    A single line containing a positive integer, n.

Output Format:
    Print Weird if the number is weird. Otherwise, print Not Weird.
"""
if __name__ == '__main__':
    n = int(input().strip())
    weird = "Weird"
    not_weird = "Not Weird"

    if n % 2 == 1:
        print(weird)
    else:
        if 2 <= n < 5 or n > 20:
            print(not_weird)
        elif 6 <= n <= 20:
            print(weird)