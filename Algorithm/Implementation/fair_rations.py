# http://www.hackerrank.com/challenges/fair-rations

n, a = int(input()), list(map(int, input().split()))
s, c = 0, 0
for v in a:
    s += v
    if s % 2 != 0:
        c += 2
print(str(c) if s % 2 == 0 else 'NO')
