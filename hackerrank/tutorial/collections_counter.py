# http://www.hackerrank.com/contests/python-tutorial/challenges/collections-counter

from collections import Counter

if __name__ == '__main__':
    x = int(input())
    c = Counter(map(int, input().split()))
    tot = 0
    for i in range(int(input())):
        s, p = map(int, input().split())
        if c[s] > 0:
            tot += p
            c[s] -= 1
    print(tot)
