# http://www.hackerrank.com/challenges/gem-stones

n = int(input())
result = set(list(input()))
for _ in range(n-1):
    s = set(list(input()))
    result = result & s
print(len(result))
