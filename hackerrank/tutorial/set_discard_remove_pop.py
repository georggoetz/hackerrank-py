# http://www.hackerrank.com/contests/python-tutorial/challenges/py-set-discard-remove-pop

n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    c = input().split()
    if c[0] == 'pop':
        s.pop()
    elif c[0] == 'remove':
        s.remove(int(c[1]))
    elif c[0] == 'discard':
        s.discard(int(c[1]))
print(sum(s))
