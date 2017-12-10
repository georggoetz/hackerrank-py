# http://www.hackerrank.com/contests/python-tutorial/challenges/np-shape-reshape/

import numpy
a = numpy.array(input().split(), int)
a.shape = (3, 3)
print(a)
