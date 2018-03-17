# htts://www.hackerrank.com/challenges/two-pluses


class Position:
    def __init__(self, r, c):
        self.row = r
        self.col = c

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)

    def __hash__(self):
        return hash(self.row) ^ hash(self.col)

    def __repr__(self):
        return '(' + str(self.row) + ', ' + str(self.col) + ')'


class Plus:
    def __init__(self, r, c, n):
        self.center = Position(r, c)
        self.length = n
        self.area = 1 + 4 * n

    def get_positions(self):
        s = set()
        for i in range(0, self.length + 1):
            s.add(Position(self.center.row - i, self.center.col))
            s.add(Position(self.center.row + i, self.center.col))
            s.add(Position(self.center.row, self.center.col - i))
            s.add(Position(self.center.row, self.center.col + i))
        return s

    def __contains__(self, other):
        s = self.get_positions().intersection(other.get_positions())
        return len(s) > 0


def makePlus(grid, r, c):
    ans = []
    n = 0
    while i-n >= 0 and grid[i-n][j] == 'G' \
            and i+n < n and grid[i+n][j] == 'G' \
            and j-n >= 0 and grid[i][j-n] == 'G' \
            and j+n < m and grid[i][j+n] == 'G':
        ans.append(Plus(r, c, n))
        n += 1
    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = []
    plus_list = []
    for _ in range(n):
        grid.append(input())
    for i in range(n):
        for j in range(m):
            plus_list.extend(makePlus(grid, i, j))
    max_area = 0
    for i in range(len(plus_list)):
        p = plus_list[i]
        for j in range(i+1, len(plus_list)):
            q = plus_list[j]
            prod_area = p.area * q.area
            if prod_area > max_area and p not in q:
                max_area = prod_area
    print(max_area)
