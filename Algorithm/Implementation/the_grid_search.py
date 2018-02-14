# http://www.hackerrank.com/challenges/the-grid-search

from re import finditer
for _ in range(int(input())):
    grid_rows, grid_cols = map(int, input().split())
    grid = []
    for _ in range(grid_rows):
        grid.append(input())
    pat_rows, pat_cols = map(int, input().split())
    pat = []
    for _ in range(pat_rows):
        pat.append(input())
    ans = 'NO'
    for grid_row in range(grid_rows):
        for m in finditer('(?=%s)' % pat[0], grid[grid_row]):
            pos = m.start()
            c = 1
            for pat_row in pat[1:]:
                if grid_row+c >= grid_rows or \
                   pat_row != grid[grid_row+c][pos:pos+pat_cols]:
                    break
                c += 1
                if c == pat_rows:
                    ans = 'YES'
                    break
    print(ans)
