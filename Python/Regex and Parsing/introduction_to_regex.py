# http://www.hackerrank.com/contests/python-tutorial/challenges/introduction-to-regex

import re
for _ in range(int(input())):
    print(bool(re.match(r'^[+-]?(\d+\.\d+$|\.\d+)', input())))
