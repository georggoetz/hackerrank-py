# http://www.hackerrank.com/contests/python-tutorial/challenges/symmetric-difference

input()
n = set(map(int, input().split()))
input()
m = set(map(int, input().split()))
a = n.difference(m).union(m.difference(n))
for i in sorted(a):
    print(i)
