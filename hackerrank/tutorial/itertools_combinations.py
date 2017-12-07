# http://www.hackerrank.com/contests/python-tutorial/challenges/itertools-combinations

from itertools import combinations
s, k = input().split()
for i in range(1, int(k)+1):
    print('\n'.join(sorted(map(lambda tup: ''.join(sorted(tup)), combinations(s, i)))))
