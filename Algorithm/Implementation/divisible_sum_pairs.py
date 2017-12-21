# http://www.hackerrank.com/challenges/divisible-sum-pairs


def divisibleSumPairs(n, k, ar):
    return len([(i, j) for i in range(n) for j in range(i+1, n) if (ar[i]+ar[j]) % k == 0])


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
