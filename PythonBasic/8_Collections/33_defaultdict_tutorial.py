"""
Task:
    In this challenge, you will be given 2 integers, n and m.
    There are n words, which might repeat, in word group A.
    There are m words belonging to word group B.
    For each m  words, check whether the word has appeared in group A or not.
    Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Input Format:
    The first line contains integers, m and n separated by a space.
    The next n lines contains the words belonging to group A.
    The next m lines contains the words belonging to group B.

Output Format:
    Output m lines.
    The ith line should contain the -indexed positions of the occurrences of the  word separated by spaces.

What I learned:
    When I use defaultdict with list, I can append values to the key.
"""

# Solution:
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(1, n + 1):
    d[input()].append(str(i))

result = []
for i in range(m):
    word = input()
    result.append(' '.join(d[word])) if word in d else result.append('-1')

print('\n'.join(result))