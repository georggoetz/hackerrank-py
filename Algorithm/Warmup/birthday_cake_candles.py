# http://www.hackerrank.com/challenges/birthday-cake-candles

from collections import Counter


def birthdayCakeCandles(n, ar):
    return Counter(ar).most_common(1)[0][1]


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
