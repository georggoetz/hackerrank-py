# http://www.hackerrank.com/contests/python-tutorial/challenges/iterables-and-iterators

from itertools import combinations
n = int(input())
a = input().split()
k = int(input())
c = list(combinations(range(1, n+1), k))
f = list(filter(lambda tup: any(a[i-1] == 'a' for i in tup), c))
print(len(f)/len(c))
