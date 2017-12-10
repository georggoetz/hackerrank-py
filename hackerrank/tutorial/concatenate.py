# http://www.hackerrank.com/contests/python-tutorial/challenges/np-concatenate

import numpy
n, m, _ = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(m)], int)
print(numpy.concatenate((a, b), axis=0))
