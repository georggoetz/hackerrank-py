# https://www.hackerrank.com/contests/python-tutorial/challenges/maximize-it

from itertools import product

k, m = map(int, input().split())
a = []
for _ in range(k):
    a.append(list(map(int, input().split()))[1:])
print(max(map(lambda tup: sum(map(lambda x: x**2, tup)) % m, product(*a))))
