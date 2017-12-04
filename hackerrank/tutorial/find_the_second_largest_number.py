# http://www.hackerrank.com/contests/python-tutorial/challenges/find-second-maximum-number-in-a-list


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr), reverse=True)[1])
