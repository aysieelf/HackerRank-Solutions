"""
Task:
    Students of District College have a subscription to English and French newspapers.
    Some students have subscribed to only the English newspaper, some have subscribed to
    only the French newspaper, and some have subscribed to both newspapers.

    You are given two sets of student roll numbers.
    One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper.
    Your task is to find the total number of students who have subscribed to only English newspapers.

    Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

Input Format:
    The first line contains the number of students who have subscribed to the English newspaper.
    The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
    The third line contains the number of students who have subscribed to the French newspaper.
    The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.


Output Format:
    Output total number of students who have subscriptions to the English or the French newspaper but not both.
"""

english = int(input())
english_set = set(input().split())
french = int(input())
french_set = set(input().split())
print(len(english_set.symmetric_difference(french_set)))