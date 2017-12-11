# http://www.hackerrank.com/contests/python-tutorial/challenges/py-collections-deque

from collections import deque
a = deque()
for _ in range(int(input())):
    op = input().split()
    if (op[0] == 'append'):
        a.append(op[1])
    elif (op[0] == 'appendleft'):
        a.appendleft(op[1])
    elif (op[0] == 'popleft'):
        a.popleft()
    elif (op[0] == 'pop'):
        a.pop()
print(' '.join(a))
