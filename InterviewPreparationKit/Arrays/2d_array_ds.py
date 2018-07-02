# http://www.hackerrank.com/challenges/2d-array/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D=interview-preparation-kit&slugs%5B%5D=arrays

a = []
for _ in range(6):
    a.append(list(map(int, input().split())))
result = -64
for j in range(4):
    for i in range(4):
        s = sum(a[j][i:i+3]) + a[j+1][i+1] + sum(a[j+2][i:i+3])
        if s > result:
            result = s
print(result)
