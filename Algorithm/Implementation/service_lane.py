# http://www.hackerrank.com/challenges/service-lane

n, t = map(int, input().split())
width = list(map(int, input().split()))
for _ in range(t):
    s, e = map(int, input().split())
    m = 3
    for i in range(s, e + 1):
        if width[i] < m:
            m = width[i]
        if m == 1:
            break
    print(m)
