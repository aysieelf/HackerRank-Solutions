"""
Task:
    In this challenge, the user enters a string and a substring.
    You have to print the number of times that the substring occurs in the given string.
    String traversal will take place from left to right, not from right to left.

Input Format:
    The first line of input contains the original string.
    The next line contains the substring.

Output Format:
Output the integer number indicating the total number of occurrences
of the substring in the original string.
"""

def count_substring(string, sub_string):
    length_sub_string = len(sub_string)
    search_range = len(string) - length_sub_string + 1

    counter = 0
    for i in range(0, search_range):
        curr_part = string[i:i+length_sub_string]
        if curr_part == sub_string:
            counter += 1

    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
