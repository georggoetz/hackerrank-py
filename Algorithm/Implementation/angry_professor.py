# http://www.hackerrank.com/challenges/angry-professor

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().strip().split(' '))
    a = map(int, input().strip().split(' '))
    s = sum([1 for i in a if i <= 0])
    print('YES' if s < k else 'NO')
