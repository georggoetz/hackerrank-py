# http://www.hackerrank.com/contests/python-tutorial/challenges/zipped

if __name__ == '__main__':
    n, x = map(int, input().split())
    a = []
    for _ in range(x):
        a.append(map(float, input().split()))
    for tup in zip(*a):
        print(sum(tup)/x)
