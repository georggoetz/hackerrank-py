# http://www.hackerrank.com/contests/python-tutorial/challenges/np-transpose-and-flatten

import numpy
a = numpy.array([input().split() for _ in range(int(input().split()[0]))], int)
print(numpy.transpose(a))
print(a.flatten())
