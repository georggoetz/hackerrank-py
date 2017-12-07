# http://www.hackerrank.com/contests/python-tutorial/challenges/itertools-combinations-with-replacement

from itertools import combinations_with_replacement
s, k = input().split()
print('\n'.join(sorted(map(lambda tup: ''.join(sorted(tup)), combinations_with_replacement(s, int(k))))))
