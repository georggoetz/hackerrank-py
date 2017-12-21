# http://www.hackerrank.com/challenges/electronics-shop


def getMoneySpent(keyboards, drives, s):
    m = -1
    for k in keyboards:
        for d in drives:
            if k + d > m and k + d <= s:
                m = k + d
    return m


s, n, m = map(int, input().strip().split(' '))
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
