# http://www.hackerrank.com/challenges/append-and-delete


def appendAndDelete(s, t, k):
    n = len(t)
    while len(s) + k > n:
        if len(s) > 0:
            s = s[:-1]
        k -= 1
    s += t[-k:]
    return 'Yes' if s == t else 'No'


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
