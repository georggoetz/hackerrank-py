# http://www.hackerrank.com/contests/python-tutorial/challenges/piling-up

from collections import deque

if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        s = []
        d = deque(map(int, input().split()))
        s.append(d.pop() if d[-1] > d[0] else d.popleft())
        while len(d) > 0:
            m = max(d[0], d[-1])
            if m > s[-1]:
                break
            d.pop() if d[-1] > d[0] else d.popleft()
        print('Yes' if len(d) == 0 else 'No')
