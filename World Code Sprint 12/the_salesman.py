# http://www.hackerrank.com/contests/world-codesprint-12


def minimumTime(x):
    a = sorted(x)
    return a[-1] - a[0]


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        x = list(map(int, input().strip().split(' ')))
        result = minimumTime(x)
        print(result)
