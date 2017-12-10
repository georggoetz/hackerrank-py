# http://www.hackerrank.com/contests/python-tutorial/challenges/np-min-and-max

import numpy
n, _ = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(numpy.max(numpy.min(a, axis=1)))
