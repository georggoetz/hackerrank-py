# http://www.hackerrank.com/contests/python-tutorial/challenges/map-and-lambda-expression


def fibonacci(n):
    f = [0] * n
    for i in range(n):
        f[i] = i if i <= 1 else f[i-1] + f[i-2]
    return f


if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x ** 3, fibonacci(n))))
