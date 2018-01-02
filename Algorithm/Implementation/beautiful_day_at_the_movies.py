# http://www.hackerrank.com/challenges/beautiful-days-at-the-movies


def reversed(n):
    sign = 1
    ans = 0
    if n < 0:
        sign = -1
    n = abs(n)
    while n > 0:
        ans *= 10
        ans += n % 10
        n //= 10
    return ans * sign


def beautifulDays(i, j, k):
    count = 0
    for n in range(i, j+1):
        if abs(n - reversed(n)) % k == 0:
            count += 1
    return count


if __name__ == "__main__":
    i, j, k = map(int, input().strip().split(' '))
    result = beautifulDays(i, j, k)
    print(result)
