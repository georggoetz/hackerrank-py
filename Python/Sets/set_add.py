# http://www.hackerrank.com/contests/python-tutorial/challenges/py-set-add

if __name__ == '__main__':
    s = set([])
    for _ in range(int(input())):
        s.add(input())
    print(len(s))
