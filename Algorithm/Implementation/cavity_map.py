# http://www.hackerrank.com/challenges/cavity-map

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, list(input()))))
for i in range(0, n):
    row = []
    for j in range(0, n):
        depth = grid[i][j]
        if i > 0 and j > 0 and i < n-1 and j < n-1 and \
           depth > grid[i-1][j] and \
           depth > grid[i][j+1] and \
           depth > grid[i+1][j] and \
           depth > grid[i][j-1]:
                row.append('X')
        else:
            row.append(str(depth))
    print(''.join(row))
