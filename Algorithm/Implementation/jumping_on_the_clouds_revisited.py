# http://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited


def jumpingOnClouds(c, k):
    n = len(c)
    p = k % n
    e = 99
    if c[p] > 0:
        e -= 2
    while p != 0:
        p = (p + k) % n
        e -= 1
        if c[p] > 0:
            e -= 2
    return e


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, k)
    print(result)
