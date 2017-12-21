# http://www.hackerrank.com/challenges/breaking-best-and-worst-records


def getRecord(s):
    min = max = s[0]
    best = worst = 0
    for i in range(1, len(s)):
        if s[i] > max:
            max = s[i]
            best += 1
        if s[i] < min:
            min = s[i]
            worst += 1
    return best, worst


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print(' '.join(map(str, result)))
