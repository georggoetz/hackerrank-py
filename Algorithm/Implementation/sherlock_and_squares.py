# http://www.hackerrank.com/challenges/sherlock-and-squares

from math import ceil, floor, sqrt


# the largest perfect square that does not exceed b minus the next perfect
# square after a
def squares(a, b):
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1


if __name__ == "__main__":
    q = int(input().strip())
    for _ in range(q):
        a, b = map(int, input().strip().split(' '))
        result = squares(a, b)
        print(result)
