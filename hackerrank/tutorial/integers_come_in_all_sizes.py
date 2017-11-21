def solve(a, b, c, d):
    """
    >>> solve(9, 29, 7, 27)
    4710194409608608369201743232
    """
    print(a ** b + c ** d)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(solve(a, b, c, d))
