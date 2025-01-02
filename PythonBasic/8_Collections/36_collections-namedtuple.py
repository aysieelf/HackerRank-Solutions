"""
Task:
    Dr. John Wesley has a spreadsheet containing a list of student's ID's, marks, class and name.
    Your task is to help Dr. Wesley calculate the average marks of the students.

    Note:
    1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
    2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format:
    The first line contains an integer N, the total number of students.
    The second line contains the names of the columns in any order.
    The next N lines contains the IDs, marks, class and names, under their respective column names.

Output Format
    Print the average marks of the list corrected to 2 decimal places.
"""
from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input())
students = [Student(*input().split()) for _ in range(n)]
print(f"{(sum(int(s.MARKS) for s in students) / n):.2f}")