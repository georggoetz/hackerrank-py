# http://www.hackerrank.com/contests/python-tutorial/challenges/no-idea

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    happiness = 0
    for val in arr:
        if val in a:
            happiness += 1
        if val in b:
            happiness -= 1
    print(happiness)
