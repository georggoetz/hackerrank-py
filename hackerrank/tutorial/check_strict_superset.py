# http://www.hackerrank.com/contests/python-tutorial/challenges/py-check-strict-superset

a = set(input().split())
b = True
for _ in range(int(input())):
    s = set(input())
    if not a.issuperset(s):
        b = False
    if len(s) >= len(a):
        b = False
print(b)
