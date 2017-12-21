# http://www.hackerrank.com/challenges/drawing-book


def solve(n, p):
    if n % 2 == 0:
        n += 1
    if p % 2 == 0:
        return min(p // 2, (n - p - 1) // 2)
    return min((p - 1) // 2, (n - p) // 2)


n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
