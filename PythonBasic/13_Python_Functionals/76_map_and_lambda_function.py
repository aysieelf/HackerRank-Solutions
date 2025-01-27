"""
Task:
    You have to generate a list of the first N fibonacci numbers, 0 being the first number.
    Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.
"""
cube = lambda x: x ** 3


def fibonacci(n):
    fib_list = []

    if n <= 0:
        return fib_list

    fib_list.append(0)

    if n == 1:
        return fib_list

    fib_list.append(1)

    for i in range(2, n):
        next_num = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_num)

    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
