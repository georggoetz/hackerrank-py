# http://www.hackerrank.com/challenges/compare-the-triplets


def solve(a0, a1, a2, b0, b1, b2):
    alice = bob = 0
    a, b = [a0, a1, a2], [b0, b1, b2]
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return alice, bob


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(' '.join(map(str, result)))
