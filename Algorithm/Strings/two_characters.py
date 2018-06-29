# http://www.hackerrank.com/challenges/two-characters/problem

from itertools import combinations

n = int(input())
s = str(input())
cs = combinations(''.join(set(s)), 2)
result = 0
for c in cs:
    j = 0
    length = 1
    for i in range(len(s)):
        if s[i] in c:
            j = i
            break
    for i in range(j+1, len(s)):
        if s[i] in c:
            if s[i] != s[j]:
                j = i
                length += 1
            else:
                length = 0
                break
    if length > result:
        result = length
print(result)
