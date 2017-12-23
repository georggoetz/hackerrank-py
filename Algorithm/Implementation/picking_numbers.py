# http://www.hackerrank.com/challenges/picking-numbers

n = int(input().strip())
a = list(map(int, input().split()))
s = {}
for n in a:
    if n in s:
        s[n].append(n)
    else:
        s[n] = [n]
for n in a:
    if n + 1 in s:
        s[n + 1].append(n)
m = 0
for k in s:
    if len(s[k]) > m:
        m = len(s[k])
print(m)
