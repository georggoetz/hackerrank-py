# http://www.hackerrank.com/challenges/the-birthday-bar


def solve(n, s, d, m):
    c = 0
    for i in range(0, n-m+1):
        if sum(s[i:i+m]) == d:
            c += 1
    return c


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = map(int, input().strip().split(' '))
result = solve(n, s, d, m)
print(result)
