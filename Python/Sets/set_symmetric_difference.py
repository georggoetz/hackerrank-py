# http://www.hackerrank.com/contests/python-tutorial/challenges/py-set-symmetric-difference-operation

n = int(input())
en = set(map(int, input().split()))
b = int(input())
fr = set(map(int, input().split()))
print(len(en.symmetric_difference(fr)))
