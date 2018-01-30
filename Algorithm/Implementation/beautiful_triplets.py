# http://www.hackerrank.com/challenges/beautiful-triplets

n, d = map(int, input().split())
a = list(map(int, input().split()))
m = {}
for i in range(n):
    m[a[i]] = i
c = 0
for i, v in enumerate(a):
    if v + d in m and v + 2*d in m and i < m[v + d] and m[v + d] < m[v + 2*d]:
        c += 1
print(c)
