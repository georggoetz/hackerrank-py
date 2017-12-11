# http://www.hackerrank.com/contests/python-tutorial/challenges/alphabet-rangoli/problem


def print_rangoli(size):
    if size <= 1:
        print('a')
        return
    n = 4*(size-1) + 1
    a = []
    for i in range(size-1, -1, -1):
        s = chr(ord('a') + i)
        for j in range(i+1, size):
            c = chr(ord('a') + j)
            s = c + '-' + s + '-' + c
        a.append(s.center(n, '-'))
    a.extend(a[size-2::-1])
    print('\n'.join(a))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
