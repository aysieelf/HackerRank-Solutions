"""
Task:
    Ms. Gabriel Williams is a botany professor at District College.
    One day, she asked her student Mickey to compute the average of all the plants
    with distinct heights in her greenhouse.

    Formula used:
        average = sum of distinct heights / total number of distinct heights

    average has the following parameters:
        int arr: an array of integers
    Returns:
        float: the resulting float value rounded to 3 places after the decimal

Input Format:
    The first line contains the integer, n, the size of arr.
    The second line contains the n space-separated integers, arr[i].
"""

def average(array):
    set_arr = set(array)

    return f"{(sum(set_arr)/len(set_arr)):.3f}"

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)