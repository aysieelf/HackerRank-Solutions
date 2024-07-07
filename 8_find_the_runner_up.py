if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    max_num = -100
    runner_up = -100

    for i in arr:
        if i > max_num:
            runner_up = max_num
            max_num = i
        elif i > runner_up and i != max_num:
            runner_up = i


    print(runner_up)
