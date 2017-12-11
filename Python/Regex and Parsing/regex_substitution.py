# http://www.hackerrank.com/contests/python-tutorial/challenges/re-sub-regex-substitution/problem

import re

if __name__ == '__main__':
    for i in range(int(input())):
        print(re.sub('(?<= )&&(?= )', 'and', re.sub('(?<= )\|\|(?= )', 'or', input())))
