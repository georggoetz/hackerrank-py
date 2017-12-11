# http://www.hackerrank.com/contests/python-tutorial/challenges/np-linear-algebra

import numpy
print(numpy.linalg.det([list(map(float, input().split())) for _ in range(int(input()))]))
