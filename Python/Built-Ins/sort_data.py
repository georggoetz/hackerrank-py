# http://www.hackerrank.com/contests/python-tutorial/challenges/python-sort-sort

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = []
    for _ in range(n):
        a.append([int(temp) for temp in input().strip().split(' ')])
    k = int(input().strip())
    for row in sorted(a, key=lambda x: x[k]):
        print(' '.join(map(str, row)))
