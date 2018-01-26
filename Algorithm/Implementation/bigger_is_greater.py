# http://www.hackerrank.com/challenges/bigger-is-greater

# Next lexicographical permutation algorithm
t = int(input().strip())
for _ in range(t):
    w = list(input())
    n = len(w)
    i = n - 1
    while i > 0 and w[i-1] >= w[i]:
        i -= 1
    if i <= 0:
        print('no answer')
    else:
        j = n - 1
        while w[j] <= w[i-1]:
            j -= 1
        w[j], w[i-1] = w[i-1], w[j]
        j = n - 1
        while i < j:
            w[i], w[j] = w[j], w[i]
            i += 1
            j -= 1
        print(''.join(w))
