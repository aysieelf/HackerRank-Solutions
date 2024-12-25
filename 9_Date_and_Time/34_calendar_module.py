"""
Task:
    You are given a date. Your task is to find what the day is on that date.

Input Format:
    A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

Output Format:
    Output the correct day in capital letters.

Sample Input

08 05 2015
Sample Output

WEDNESDAY
"""
from calendar import weekday

month, day, year = input().split()

day_of_week_number = weekday(int(year), int(month), int(day))

days_of_week = {
    0:"MONDAY",
    1:"TUESDAY",
    2:"WEDNESDAY",
    3:"THURSDAY",
    4:"FRIDAY",
    5:"SATURDAY",
    6:"SUNDAY"
}

print(days_of_week[day_of_week_number])