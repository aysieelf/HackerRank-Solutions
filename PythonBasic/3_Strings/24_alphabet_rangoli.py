"""
Task:

    You are given an integer, N. Your task is to print an alphabet rangoli of size N.
    (Rangoli is a form of Indian folk art based on creation of patterns.)

    Different sizes of alphabet rangoli are shown below:

    #size 3

    ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----

    #size 5

    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------

    The center of the rangoli has the first alphabet letter a,
    and the boundary has the Nth alphabet letter (in alphabetical order).

    rangoli has the following parameters:
        int size: the size of the rangoli
    Returns:
        string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

Input Format:
Only one line of input containing N, the size of the rangoli.
"""

def print_rangoli(size):
    letter_a_ascii = 97
    last_letter_ascii = letter_a_ascii + size
    width = size * 4 - 3
    upper_part = []

    # upper part
    for i in range(1, size+1):
        letters = []
        for ii in range(i, 0, -1):
            letters.append(chr(last_letter_ascii - ii))
            if len(letters) > 1:
                letters.insert(0, chr(last_letter_ascii - ii))
        upper_part.append('-'.join(letters).center(width, '-'))

    # lower part
    lower_part = [row for row in upper_part[-2::-1]]
    result = upper_part + lower_part
    print('\n'.join(result))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)