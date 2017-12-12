# http://www.hackerrank.com/challenges/mini-max-sum

a = list(sorted(map(int, input().strip().split())))
print(sum(a[:4]), sum(a[1:]))
