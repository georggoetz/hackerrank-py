# http://www.hackerrank.com/contests/python-tutorial/challenges/np-polynomials

import numpy
print(numpy.polyval(list(map(float, input().split())), float(input())))
