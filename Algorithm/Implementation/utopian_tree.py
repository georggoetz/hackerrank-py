# http://www.hackerrank.com/challenges/utopian-tree

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    h = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            h += 1
        else:
            h = h << 1
    print(h)
