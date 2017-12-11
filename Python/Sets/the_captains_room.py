# http://www.hackerrank.com/contests/python-tutorial/challenges/py-the-captains-room

from collections import Counter
k = int(input())
print(Counter(map(int, input().split())).most_common()[-1][0])
