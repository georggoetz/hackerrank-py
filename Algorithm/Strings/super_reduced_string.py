# https://www.hackerrank.com/challenges/reduced-string


def reduce(s):
    ans = []
    for c in s:
        if len(ans) > 0 and ans[-1] == c:
            ans.pop()
        else:
            ans.append(c)
    return ans


if __name__ == '__main__':
    s = list(input().strip())
    n = len(s)
    while True:
        s = reduce(s)
        if len(s) < n:
            n = len(s)
        else:
            break
    print('Empty String' if len(s) == 0 else ''.join(s))
