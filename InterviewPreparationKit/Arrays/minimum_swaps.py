# http://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D=interview-preparation-kit&slugs%5B%5D=arrays

n = int(input())
a = list(map(int, input().split()))
c = 0
i = 0
while i < n:
    if i+1 != a[i]:
        a[a[i]-1], a[i] = a[i], a[a[i]-1]
        c += 1
    else:
        i += 1
print(c)
