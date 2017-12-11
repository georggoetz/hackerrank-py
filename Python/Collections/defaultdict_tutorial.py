# http://www.hackerrank.com/contests/python-tutorial/challenges/defaultdict-tutorial

from collections import defaultdict

if __name__ == '__main__':
    d = defaultdict(list)
    n, m = map(int, input().split())
    for i in range(n):
        d[input()].append(i+1)
    for i in range(m):
        key = input()
        print(' '.join(map(str, d[key])) if key in d else -1)
