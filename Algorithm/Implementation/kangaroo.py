# http://www.hackerrank.com/challenges/kangaroo


def kangaroo(x1, v1, x2, v2):
    return 'NO' if v1 <= v2 or abs(x1-x2) % abs(v1-v2) != 0 else 'YES'


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
