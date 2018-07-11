# http://www.hackerrank.com/challenges/the-love-letter-mystery

q = int(input())
for _ in range(q):
    a = list(input())
    i, j, count = 0, len(a) - 1, 0
    while i < j:
        while ord(a[i]) < ord(a[j]):
            a[j] = chr(ord(a[j]) - 1)
            count += 1
        while ord(a[j]) < ord(a[i]):
            a[i] = chr(ord(a[i]) - 1)
            count += 1
        i += 1
        j -= 1
    print(count)
