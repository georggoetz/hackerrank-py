# http://www.hackerrank.com/contests/world-codesprint-12/challenges/breaking-sticks

from math import sqrt


def divisor(n):
    if n % 2 == 0:
        return n // 2
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return n // i
    return 1


def longestSequence(a):
    sum = 0
    for n in a:
        while n > 1:
            sum += n
            n = divisor(n)
        sum += 1
    return sum


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = longestSequence(a)
    print(result)
