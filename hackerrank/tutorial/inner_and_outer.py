# http://www.hackerrank.com/challenges/np-inner-and-outer

import numpy
a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)
print(numpy.inner(a, b))
print(numpy.outer(a, b))
