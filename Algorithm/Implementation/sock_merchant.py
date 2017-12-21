# http://www.hackerrank.com/challenges/sock-merchant

from collections import Counter


def sockMerchant(n, ar):
    return sum([item[1] // 2 for item in Counter(ar).most_common()])


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
