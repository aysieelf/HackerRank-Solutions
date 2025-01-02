"""
Task:
    Given the names and grades for each student in a class of N students,
    store them in a nested list and print the name(s) of any student(s)
    having the second lowest grade.

    Note: If there are multiple students with the second lowest grade,
    order their names alphabetically and print each name on a new line.

Input Format:

    The first line contains an integer, N, the number of students.
    The 2N subsequent lines describe each student over 2 lines.
    - The first line contains a student's name.
    - The second line contains their grade.

Output Format:

    Print the name(s) of any student(s) having the second lowest grade in.
    If there are multiple students,
    order their names alphabetically and print each one on a new line.
"""

if __name__ == '__main__':
    student_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        student_scores.append([name, score])
    all_scores = [score for student, score in student_scores]
    second_lowest_score = sorted(list(set(all_scores)))[1] if len(all_scores) > 1 else all_scores[0]
    students = [student for student, score in student_scores if score == second_lowest_score]

    print('\n'.join(sorted(students)))



#
# n = int(input())
# student_scores = []
#
# for _ in range(n):
#     temp_line = [input(), float(input())]
#     student_scores.append(temp_line)
#
# score_first = 100
# score_second = 100
# for lst in student_scores:
#     if lst[1] < score_first:
#         score_second = score_first
#         score_first = lst[1]
#     elif lst[1] < score_second and lst[1] != score_first:
#         score_second = lst[1]
#
# names = []
# for second in student_scores:
#     if second[1] == score_second:
#         names.append(second[0])
#
# names.sort()
#
# print('\n'.join(names))
