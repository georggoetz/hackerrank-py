# http://www.hackerrank.com/challenges/crush/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D=interview-preparation-kit&slugs%5B%5D=arrays

n, m = map(int, input().split())
arr = [0] * (n+1)
for _ in range(m):
    a, b, k = map(int, input().split())
    arr[a] += k
    if b+1 <= n:
        arr[b+1] -= k
result = 0
s = 0
for i in range(1, n+1):
    s += arr[i]
    if s > result:
        result = s
print(result)
