"""
Task:
    The National University conducts an examination of N students in X subjects.
    Your task is to compute the average scores of each student.
        Average score = Sum of scores obtained in all subjects by a student / Total number of subjects

    The format for the general mark sheet is:
        Student ID → ___1_____2_____3_____4_____5__
        Subject 1   |  89    90    78    93    80
        Subject 2   |  90    91    85    88    86
        Subject 3   |  91    92    83    89    90.5
        __________________________________________
        Average        90    91    82    90    85.5

Input Format:
    The first line contains N and X separated by a space.
    The next X lines contains the space separated marks obtained by students in a particular subject.

Output Format:
    Print the averages of all students on separate lines.
    The average must be correct up to 1 decimal place.
"""
students, subjects = map(int, input().split())

marks = [list(map(float, input().split())) for _ in range(subjects)]

for student in zip(*marks):
    print(sum(student) / len(student))