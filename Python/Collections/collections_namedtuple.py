# http://www.hackerrank.com/contests/python-tutorial/challenges/py-collections-namedtuple

from collections import namedtuple
n = int(input())
Row = namedtuple('Row', input().split())
print(sum(int(row.MARKS) for row in [Row(*(input().split())) for _ in range(n)])/n)
