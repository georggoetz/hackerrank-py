# http://www.hackerrank.com/challenges/magic-square-formin

# see http://en.wikipedia.org/wiki/Magic_square
#
# 8	1 6
# 3	5 7
# 4	9 2
#
# Reflected:
# 8	1 6|6 1 8
# 3	5 7|7 5 3
# 4	9 2|2 9 4
# -----------
# 4 9 2|2 9 4
# 3 5 7|7 5 3
# 8 1 6|6 1 8
#
# Rotated and reflected:
# 4 3 8|8 3 4
# 9 5 1|1 5 9
# 2 7 6|6 7 2
# -----------
# 2 7 6|6 7 2
# 9 5 1|1 5 9
# 4 3 8|8 3 4

# enumerate all possible solutions
mm = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    ]

s = []
for _ in range(3):
    s.append(list(map(int, input().split())))

# then find the solution with the minimum cost to the given configuration
min_cost = 1000
for m in mm:
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(s[i][j] - m[i][j])
    if cost < min_cost:
        min_cost = cost
print(min_cost)
