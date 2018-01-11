# http://www.hackerrank.com/challenges/strange-advertising


def recurse(n, p):
    if n <= 0:
        return 0
    like = p // 2
    return like + recurse(n - 1, like * 3)


def viralAdvertising(n):
    return recurse(n, 5)


if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
