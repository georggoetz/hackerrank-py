# http://www.hackerrank.com/challenges/alternating-characters

t = int(input())
for _ in range(t):
    s = list(input())
    prev, count = s[0], 0
    for i in range(1, len(s)):
        if prev == s[i]:
            count += 1
        prev = s[i]
    print(count)
