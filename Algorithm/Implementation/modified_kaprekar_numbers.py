# http://www.hackerrank.com/challenges/kaprekar-numbers

p = int(input())
q = int(input())
a = []
for n in range(p, q+1):
    nsq = n ** 2
    s = str(nsq)
    l2 = len(s) // 2
    ls, rs = s[0:l2], s[l2:]
    left = 0 if len(ls) == 0 else int(ls)
    right = 0 if len(rs) == 0 else int(rs)
    if left + right == n:
        a.append(n)
print(' '.join(map(str, a)) if len(a) > 0 else 'INVALID RANGE')
