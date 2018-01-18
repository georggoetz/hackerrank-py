# http://www.hackerrank.com/challenges/equality-in-a-array

from collections import Counter


def equalizeArray(arr):
    c = Counter(arr)
    return sum(map(lambda x: x[1], c.most_common()[1:])) if len(c) > 1 else 0


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
