n = int(input())
student_scores = []

for _ in range(n):
    temp_line = [input(), float(input())]
    student_scores.append(temp_line)

score_first = 100
score_second = 100
for lst in student_scores:
    if lst[1] < score_first:
        score_second = score_first
        score_first = lst[1]
    elif lst[1] < score_second and lst[1] != score_first:
        score_second = lst[1]

names = []
for second in student_scores:
    if second[1] == score_second:
        names.append(second[0])

names.sort()

print('\n'.join(names))
