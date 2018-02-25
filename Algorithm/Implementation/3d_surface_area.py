# http://www.hackerrank.com/challenges/3d-surface-area

h, w = map(int, input().split())
a = []
surface = 0
for i in range(h):
    a.append(list(map(int, input().split())))
    for j in range(w):
        surface += 2 + a[i][j] * 4
        d = 0
        if i > 0:
            d += 2 * min(a[i-1][j], a[i][j])
        if j > 0:
            d += 2 * min(a[i][j-1], a[i][j])
        surface -= d
print(surface)
