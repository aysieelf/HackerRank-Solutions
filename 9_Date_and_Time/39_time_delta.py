"""
Task:
    When users post an update on social media, such as a URL, image, status update etc.,
    other users in their network are able to view this new post on their news feed.
    Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

    Since sometimes posts are published and viewed in different time zones, this can be confusing.
    You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

    Day dd Mon yyyy hh:mm:ss +xxxx
    Sun 10 May 2015 13:54:36 -0700

    Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format:
    The first line contains t, the number of testcases.
    Each testcase contains 2 lines, representing time t1 and time t2.

Output Format:
    Print the absolute difference (t1 - t2) in seconds.

WHAT I LEARNED:
    I can use the datetime module to convert the string to a datetime object
        %a is the abbreviated weekday name
        %d is the day of the month
        %B is the full month name, %b is the abbreviated month name
        %Y is the full year, %y is only the last two digits
        %H is the hour in 24-hour format
        %M is the minute
        %S is the second
        %z is the timezone offset
    I can then use the subtraction operator to get the difference between the two datetime objects which
        will return a timedelta object
    I can then use the .seconds method to get the difference in seconds
    I can also use the .days method to get the difference in days

"""
from datetime import datetime


def time_delta(t1, t2):
    datetime_format = "%a %d %b %Y %H:%M:%S %z"
    d1 = datetime.strptime(t1, datetime_format)
    d2 = datetime.strptime(t2, datetime_format)
    difference = abs((d2 - d1))
    total_seconds = difference.days * 24 * 60 * 60 + difference.seconds
    return str(total_seconds)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)
