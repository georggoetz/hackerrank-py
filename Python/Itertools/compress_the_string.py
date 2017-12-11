# http://www.hackerrank.com/contests/python-tutorial/challenges/compress-the-string

from itertools import groupby
print(*[(len(list(g)), int(k)) for k, g in groupby(input())])
