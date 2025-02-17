"""
Task:
    Raghu is a shoe shop owner. His shop has X number of shoes.
    He has a list containing the size of each shoe he has in his shop.
    There are N number of customers who are willing to pay xi amount of money
    only if they get the shoe of their desired size.

    Your task is to compute how much money Raghu earned.

Input Format:
    The first line contains X, the number of shoes.
    The second line contains the space separated list of all the shoe sizes in the shop.
    The third line contains N, the number of customers.
    The next N lines contain the space separated values of the show size desired by the customer
    and xi, the price of the shoe.

Output Format:
    Print the amount of money earned by Raghu.

What I learned:
    A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
"""
from collections import Counter

shoes_count = int(input())
shoes_sizes = list(map(int, input().split()))
customers_count = int(input())

ttl_shoes = Counter(shoes_sizes)

result = 0
for _ in range(customers_count):
    shoe_size, price = map(int, input().split())

    if ttl_shoes[shoe_size] != 0:
        ttl_shoes[shoe_size] -= 1
        result += price


print(result)
