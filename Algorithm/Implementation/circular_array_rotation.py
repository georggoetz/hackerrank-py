# http://www.hackerrank.com/challenges/circular-array-rotation

from fractions import gcd


# Too slow...
'''
def rotateRight(a, k):
    n = len(a)
    if n < 2:
        return
    for _ in range(k):
        t = a[n-1]
        for i in range(n-1, 0, -1):
            a[i] = a[i-1]
        a[0] = t
'''


# The juggling algorithm. Left rotates array a by k positions. If k is negative
# performs right rotation.
def rotate(a, k):
    n = len(a)
    # Handle negative values - i.e. rotate right instead of left
    if k < 0:
        k = n + k
    # Ensure that k <= n
    k = k % n
    for i in range(0, gcd(n, k)):
        t = a[i]
        j = i
        while True:
            p = j + k
            if p >= n:
                p = p - n
            if p == i:
                break
            a[j] = a[p]
            j = p
        a[j] = t


def circularArrayRotation(a, k, m):
    rotate(a, -k)
    return [a[i] for i in m]


if __name__ == "__main__":
    n, k, q = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    m = []
    for _ in range(q):
        m.append(int(input().strip()))
    result = circularArrayRotation(a, k, m)
    print('\n'.join(map(str, result)))
