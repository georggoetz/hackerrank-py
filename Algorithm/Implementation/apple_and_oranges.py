# http://www.hackerrank.com/challenges/apple-and-orange


def count_in(a, start, end):
    c = 0
    for n in a:
        if n >= start and n <= end:
            c += 1
    return c


s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apples = [a + int(apple) for apple in input().strip().split(' ')]
print(count_in(apples, s, t))
oranges = [b + int(orange) for orange in input().strip().split(' ')]
print(count_in(oranges, s, t))
