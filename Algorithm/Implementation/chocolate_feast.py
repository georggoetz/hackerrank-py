# http://www.hackerrank.com/challenges/chocolate-feast

for _ in range(int(input())):
    n, c, m = map(int, input().split())
    get_choc = n // c
    sum_choc = get_choc
    num_wraps = get_choc
    while get_choc > 0:
        get_choc = num_wraps // m
        num_wraps -= get_choc * m
        num_wraps += get_choc
        sum_choc += get_choc
    print(sum_choc)
