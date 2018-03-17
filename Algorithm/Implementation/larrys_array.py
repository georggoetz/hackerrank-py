# http://www.hackerrank.com/challenges/larrys-array

# see: http://de.wikipedia.org/wiki/Vorzeichen_(Permutation)
# (1) A rotation does not change the signum of a permutation.
# (2) The sorted list does't have any inversions, therefore sign = (-1)**0 = 0
# (3) The number of inversion must thius be even.
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    inv = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                inv += 1
    print('YES' if inv % 2 == 0 else 'NO')
