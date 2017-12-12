# http://www.hackerrank.com/challenges/between-two-sets


def getTotalX(a, b):
    cc = [0] * 101
    for i in a:
        for j in range(i, 101, i):
            cc[j] += 1
    for i in b:
        for j in range(1, j+1):
            if i % j == 0:
                cc[j] += 1
    n = len(a)+len(b)
    return len([c for c in cc if c == n])


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total = getTotalX(a, b)
    print(total)
