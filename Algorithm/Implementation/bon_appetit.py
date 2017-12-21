# http://www.hackerrank.com/challenges/bon-appetit


def bonAppetit(n, k, b, ar):
    bactual = sum([n for i, n in enumerate(ar) if i != k]) // 2
    return 'Bon Appetit' if b - bactual <= 0 else str(b - bactual)


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
