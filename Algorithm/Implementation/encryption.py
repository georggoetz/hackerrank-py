# http://www.hackerrank.com/challenges/encryption

from math import sqrt, floor, ceil

str = input().strip()
n = len(str)
nsqrt = sqrt(n)
rows, cols = floor(nsqrt), ceil(nsqrt)
if rows * cols < n:
    rows = ceil(nsqrt)
ans = ""
for i in range(cols):
    for j in range(rows):
        pos = i + cols * j
        if pos < n:
            ans += str[pos]
    ans += " "
print(ans)
