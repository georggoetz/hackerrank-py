# http://www.hackerrank.com/challenges/hackerrank-in-a-string

q = int(input())
w = 'hackerrank'

for _ in range(q):
    s = input()
    j = 0
    for c in s:
        if j == len(w):
            break
        if c == w[j]:
            j += 1
    print('YES' if j == len(w) else 'NO')
