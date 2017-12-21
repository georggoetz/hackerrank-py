# http://www.hackerrank.com/challenges/migratory-birds

from collections import Counter


def migratoryBirds(n, ar):
    return sorted([tup[0] for tup in Counter(ar).most_common(1)])[0]


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
