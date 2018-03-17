# http://www.hackerrank.com/challenges/bomber-man


def print_grid(grid):
    for i in range(len(grid)):
        print(''.join(grid[i]))


def blow_up(grid1, grid2):
    for i in range(r):
        for j in range(c):
            if grid1[i][j] == 'O':
                grid2[i][j] = '.'
                if i + 1 < r:
                    grid2[i + 1][j] = '.'
                if i - 1 >= 0:
                    grid2[i - 1][j] = '.'
                if j + 1 < c:
                    grid2[i][j + 1] = '.'
                if j - 1 >= 0:
                    grid2[i][j - 1] = '.'


if __name__ == '__main__':
    r, c, n = map(int, input().split())
    if n > 0 and n % 2 == 0:
        for i in range(r):
            print('O' * c)
    else:
        initial_grid = []
        grid1 = []
        grid2 = []
        for i in range(r):
            initial_grid.append([])
            grid1.append([])
            grid2.append([])
            for v in input():
                initial_grid[i].append(v)
                grid1[i].append('O')
                grid2[i].append('O')
        if n < 2:
            print_grid(initial_grid)
        else:
            blow_up(initial_grid, grid1)
            if n % 4 == 3:
                print_grid(grid1)
            else:
                blow_up(grid1, grid2)
                print_grid(grid2)

# t = 0
# .......
# ...O...
# ....O..
# .......
# OO.....
# OO.....
#
# t = 1
# .......
# ...O...
# ....O..
# .......
# OO.....
# OO.....
#
# t = 2
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
#
# t = 3
# OOO.OOO
# OO...OO
# OOO...O
# ..OO.OO
# ...OOOO
# ...OOOO
#
# t = 4
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
#
# t = 5
# .......
# ...O...
# ....O..
# .......
# OO.....
# OO.....
#
# t = 6
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
#
# t = 7
# OOO.OOO
# OO...OO
# OOO...O
# ..OO.OO
# ...OOOO
# ...OOOO
