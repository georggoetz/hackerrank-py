# http://www.hackerrank.com/contests/python-tutorial/challenges/incorrect-regex

import re

for _ in range(int(input())):
    isvalid = True
    try:
        re.compile(input())
    except re.error:
        isvalid = False
    print(isvalid)
