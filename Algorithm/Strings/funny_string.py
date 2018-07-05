# https://www.hackerrank.com/challenges/funny-string

t = int(input())
for _ in range(t):
    s = list(map(ord, list(input())))
    r = s[::-1]
    funny = True
    for i in range(len(s)-1):
        ds = abs(s[i+1]-s[i])
        rs = abs(r[i+1]-r[i])
        if ds != rs:
            funny = False
            break
    print('Funny' if funny else 'Not Funny')
