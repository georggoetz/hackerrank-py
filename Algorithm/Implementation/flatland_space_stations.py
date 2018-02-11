# http://www.hackerrank.com/challenges/flatland-space-stations/problem

n, m = map(int, input().split())
c = list(map(int, input().split()))
c.sort()
dist = []
for i in range(m):
    if i == 0:
        dist.append(c[i])
    if i > 0:
        dist.append((c[i] - c[i - 1]) // 2)
    if i == m - 1:
        dist.append(n - c[i] - 1)
print(max(dist))
