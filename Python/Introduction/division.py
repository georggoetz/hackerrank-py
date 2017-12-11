# http://www.hackerrank.com/contests/python-tutorial/challenges/python-division


def solve(a, b):
    """
    >>> solve(4, 3)
    1
    1.3333333333333333
    """
    print(a//b)
    print(a/b)


if __name__ == '__main__':
    solve(int(input()), int(input()))
