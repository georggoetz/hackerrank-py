# http://www.hackerrank.com/challenges/separate-the-numbers/problem

q = int(input())
for _ in range(q):
    s = list(input())
    n, m = len(s), 1
    if n > 0 and s[0] == '0':
        print('NO')
        continue
    i = 0
    result = []
    c = ''
    while i < n-m:
        a = int(''.join(s[i:i+m]))
        b = str(a+1)
        c = ''.join(s[i+m:i+m+len(b)])
        if b == c:
            result.append(str(a))
            i += m
            m = len(b)
        else:
            result = []
            i = 0
            m += 1
    result.append(c)
    print('YES ' + result[0] if ''.join(result) == ''.join(s) else 'NO')
