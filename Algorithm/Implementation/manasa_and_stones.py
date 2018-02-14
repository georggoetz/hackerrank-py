# http://www.hackerrank.com/challenges/manasa-and-stones

for _ in range(int(input())):
    n = int(input())
    d = [int(input()), int(input())]
    a, b = min(d), max(d)
    if a == b:
        print((n - 1) * a)
    else:
        s = []
        for i in range(n):
            s.append((n - i - 1) * a + i * b)
        print(' '.join(map(str, s)))
