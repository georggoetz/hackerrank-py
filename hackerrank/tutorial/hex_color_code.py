# http://www.hackerrank.com/contests/python-tutorial/challenges/hex-color-code

import re

for i in range(int(input())):
    m = re.findall(r'[^#]+(#(?:[A-f0-9]{3}){1,2})', input())
    if m:
        print('\n'.join(m))
