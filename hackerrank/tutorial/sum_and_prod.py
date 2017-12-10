# http://www.hackerrank.com/contests/python-tutorial/challenges/np-sum-and-prod

import numpy
n, _ = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(a, axis=0)))
