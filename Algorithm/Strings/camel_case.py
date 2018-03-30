# http://www.hackerrank.com/challenges/camelcase

s = list(input().strip())
count = 1
for c in s:
    if c.isupper():
        count += 1
print(count)
