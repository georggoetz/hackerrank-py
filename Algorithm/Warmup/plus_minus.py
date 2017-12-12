# http://www.hackerrank.com/challenges/plus-minus

n = int(input().strip())
a = list(map(int, input().split()))
pos = neg = zero = 0
for i in a:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1
print(pos/n)
print(neg/n)
print(zero/n)
