# http://www.hackerrank.com/challenges/find-digits/problem

t = int(input())
for _ in range(t):
    n = int(input())
    digits = [int(c) for c in str(n)]
    print(sum([1 for d in digits if d != 0 and n % d == 0]))
