# http://www.hackerrank.com/contests/python-tutorial/challenges/itertools-permutations

from itertools import permutations
s, k = input().split()
print('\n'.join(map(lambda tup: ''.join(tup), sorted(permutations(s, int(k))))))
