# http://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D=interview-preparation-kit&slugs%5B%5D=arrays

_, d = list(map(int, input().split()))
a = list(map(int, input().split()))
print(' '.join(map(str, (a[:d][::-1] + a[d:][::-1])[::-1])))
