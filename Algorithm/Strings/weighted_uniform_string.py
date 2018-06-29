# http://www.hackerrank.com/challenges/weighted-uniform-string


def weight(c):
    return ord(c) - ord('a') + 1


s = input()
n = int(input())
w = set()
w.add(weight(s[0]))
j = 0
for i in range(1, len(s)):
    if s[i] == s[j]:
        w.add((i-j+1) * weight(s[i]))
    else:
        j = i
        w.add(weight(s[i]))
for _ in range(n):
    i = int(input())
    print('Yes' if i in w else 'No')
