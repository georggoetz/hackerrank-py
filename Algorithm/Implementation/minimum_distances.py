# http://www.hackerrank.com/challenges/minimum-distance

n = int(input())
a = list(map(int, input().split()))
m = {}
for i, v in enumerate(a):
    if v not in m:
        m[v] = [i]
    else:
        m[v].append(i)
d = -1
for k, v in m.items():
    for i in range(len(v) - 1):
        if d < 0 or v[i+1] - v[i] < d:
            d = v[i+1] - v[i]
print(d)
