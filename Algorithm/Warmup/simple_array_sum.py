# http://www.hackerrank.com/challenges/simple-array-sum


def simpleArraySum(n, ar):
    return sum(ar)


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
