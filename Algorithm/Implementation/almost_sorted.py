# https://www.hackerrank.com/challenges/almost-sorted

n = int(input())
a = list(map(int, input().split()))
expected = sorted(a)
d = []
for i in range(n):
    if a[i] != expected[i]:
        d.append(i)
if len(d) == 2:
    print('yes')
    print('swap', d[0] + 1, d[1] + 1)
else:
    sub = list(a[d[0]:d[-1]+1])
    if sub == sorted(sub, reverse=True):
        print('yes')
        print('reverse', d[0] + 1, d[-1] + 1)
    else:
        print('no')
