# http://www.hackerrank.com/contests/python-tutorial/challenges/matrix-script

import itertools
import re

n, m = map(int, input().strip().split(' '))
mat = []
for _ in range(n):
    mat.append(input().ljust(m))
s = ''.join(itertools.chain(*zip(*mat)))
print(re.sub(r'(?<=[a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])', ' ', s))
