# http://www.hackerrank.com/challenges/organizing-containers-of-balls

q = int(input().strip())
for _ in range(q):
    n = int(input().strip())
    m = []
    c, t = [0] * n, [0] * n
    # Count the number of elements in each container (rows)
    # Count the number of different types (columns)
    for i in range(n):
        for j, v in enumerate(map(int, input().strip().split(' '))):
            c[i] += v
            t[j] += v
    # By swapping elements the number of elements in each container does not
    # change.
    # Neither does the number of different types change.
    # Check if the number of elements in each container equals the number af
    # any type.
    c.sort()
    t.sort()
    ans = 'Possible'
    for i in range(n):
        if c[i] != t[i]:
            ans = 'Impossible'
            break
    print(ans)
