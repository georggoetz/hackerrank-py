# http://www.hackerrank.com/challenges/jumping-on-the-clouds


def jumpingOnClouds(c, n):
    i, j = 0, 0
    while i != n-1:
        i += 2 if i < n-2 and c[i+2] == 0 else 1
        j += 1
    return j


if __name__ == "__main__":
    n = int(input().strip())
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, n)
    print(result)
