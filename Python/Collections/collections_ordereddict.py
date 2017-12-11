# http://www.hackerrank.com/contests/python-tutorial/challenges/py-collections-ordereddict

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    k, v = input().rsplit(' ', 1)
    if k in d:
        d[k] += int(v)
    else:
        d[k] = int(v)
for k in d:
    print(k, d[k])
