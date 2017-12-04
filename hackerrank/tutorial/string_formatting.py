# http://www.hackerrank.com/contests/python-tutorial/challenges/python-string-formatting

import string


def print_formatted(number):
    w = len(format(number, 'b'))
    s = '{0:>'+str(w)+'d} {1:>'+str(w)+'o} {2:>'+str(w)+'X} {3:>'+str(w)+'b}'
    for i in range(1, number+1):
        print(s.format(i, i, i, i))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
