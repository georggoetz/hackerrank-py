# http://www.hackerrank.com/contests/world-codesprint-12/challenges/red-knights-shortest-path

from collections import deque
from collections import namedtuple


class Position(namedtuple('Position', 'i j move')):
    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def next(self, n):
        return filter(lambda p: p.i >= 0 and p.i < n and p.j >= 0 and p.j < n,
            [Position(self.i-2, self.j-1, 'UL'),
             Position(self.i-2, self.j+1, 'UR'),
             Position(self.i, self.j+2, 'R'),
             Position(self.i+2, self.j+1, 'LR'),
             Position(self.i+2, self.j-1, 'LL'),
             Position(self.i, self.j-2, 'L')])


def printShortestPath(n, i_start, j_start, i_end, j_end):
    start = Position(i_start, j_start, None)
    end = Position(i_end, j_end, None)
    prev = []
    visited = []
    for i in range(n):
        prev.append([])
        visited.append([])
        for j in range(n):
            prev[i].append(None)
            visited[i].append(False)
    q = deque()
    q.append(Position(i_start, j_start, None))
    while len(q) > 0:
        u = q.popleft()
        visited[u.i][u.j] = True
        if u == end:
            path = [u.move]
            while prev[u.i][u.j] is not None:
                if prev[u.i][u.j].move != start:
                    path.append(prev[u.i][u.j].move)
                u = prev[u.i][u.j]
            print(len(path))
            print(*path[::-1], sep=' ')
            return
        for v in u.next(n):
            if not visited[v.i][v.j]:
                visited[v.i][v.j] = True
                prev[v.i][v.j] = u
                q.append(v)
    print('Impossible')


if __name__ == "__main__":
    n = int(input().strip())
    i_start, j_start, i_end, j_end = map(int, input().strip().split(' '))
    printShortestPath(n, i_start, j_start, i_end, j_end)
