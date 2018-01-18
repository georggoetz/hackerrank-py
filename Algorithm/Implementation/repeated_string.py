# http://www.hackerrank.com/challenges/repeated-string


def repeatedString(s, n):
    m = len(s)
    num = n // m
    rem = n % m
    return s.count('a') * num + s[:rem].count('a')


if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
