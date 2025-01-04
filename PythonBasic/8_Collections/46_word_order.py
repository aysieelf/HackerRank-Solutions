"""
Task:
    You are given n words. Some words may repeat.
    For each word, output its number of occurrences.
    The output order should correspond with the input order of appearance of the word.
    See the sample input/output for clarification.

    Note: Each input line ends with a "\n" character.

Constraints:
    All the words are composed of lowercase English letters only.

Input Format:
    The first line contains the integer, n.
    The next n lines each contain a word.

Output Format:
    On the first line, output the number of distinct words from the input.
    On the second line, output the number of occurrences
    for each distinct word according to their appearance in the input.
"""
from collections import defaultdict

occurrences = defaultdict(int)
n = int(input())
for _ in range(n):
    occurrences[input()] += 1

print(len(occurrences))
result = [str(value) for value in occurrences.values()]
print(' '.join(result))