# http://www.hackerrank.com/contests/python-tutorial/challenges/python-arithmetic-operators


def solve(a, b):
    """
    >>> solve(3, 2)
    5
    1
    6
    """
    print(a+b)
    print(a-b)
    print(a*b)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    solve(a, b)
