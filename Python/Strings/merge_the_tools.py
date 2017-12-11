# http://www.hackerrank.com/contests/python-tutorial/challenges/merge-the-tools

from collections import OrderedDict


def merge_the_tools(string, k):
    for s in [string[i:i+k] for i in range(0, len(string), k)]:
        d = OrderedDict()
        for c in s:
            d[c] = True
        print(''.join([x for x in d]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
