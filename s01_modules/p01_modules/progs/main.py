from sys import path

for p in path:
    print(p)

from modules.module import sum_list, prod_list

zeroes = [0 for _ in range(5)]
ones = [1 for _ in range(5)]
print(sum_list(zeroes))
print(prod_list(ones))
