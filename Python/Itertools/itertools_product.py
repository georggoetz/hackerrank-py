# http://www.hackerrank.com/contests/python-tutorial/challenges/itertools-product

from itertools import product
a = map(int, input().split())
b = map(int, input().split())
print(' '.join(map(str, list(product(a, b)))))
