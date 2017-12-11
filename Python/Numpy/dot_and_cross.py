# http://www.hackerrank.com/contests/python-tutorial/challenges/np-dot-and-cross

import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))
