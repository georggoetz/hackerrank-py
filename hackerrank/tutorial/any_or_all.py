# http://www.hackerrank.com/contests/python-tutorial/challenges/any-or-all

n = int(input())
a = input().split()
print(all(int(v) >= 0 for v in a) and any(v == v[::-1] for v in a))
