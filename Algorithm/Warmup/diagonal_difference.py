# http://www.hackerrank.com/challenges/diagonal-difference

n = int(input().strip())
a = []
for _ in range(n):
    a.append(list(map(int, input().strip().split())))
print(abs(sum([a[i][i] for i in range(n)]) - sum([a[n-i-1][i] for i in range(n)])))
