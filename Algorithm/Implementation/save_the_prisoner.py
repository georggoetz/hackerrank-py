# http://www.hackerrank.com/challenges/save-the-prisoner


def saveThePrisoner(n, m, s):
    p = (s+m-1) % n
    return p if p != 0 else n


t = int(input().strip())
for _ in range(t):
    n, m, s = map(int, input().strip().split(' '))
    result = saveThePrisoner(n, m, s)
    print(result)
