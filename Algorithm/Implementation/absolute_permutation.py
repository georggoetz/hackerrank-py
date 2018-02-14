# http://www.hackerrank.com/challenges/absolute-permutation

from collections import Counter
for _ in range(int(input())):
    n, k = map(int, input().split())
    p = []
    c = Counter()
    for i in range(1, n+1):
        a = [i - k, i + k]
        ln = len(p)
        for j in a:
            if 1 <= j <= n and j not in c:
                p.append(j)
                c[j] += 1
                break
        if (len(p) == ln):
            p = [-1]
            break
    print(' '. join(map(str, p)))
