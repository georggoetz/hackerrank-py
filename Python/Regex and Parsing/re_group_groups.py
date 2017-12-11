# http://www.hackerrank.com/contests/python-tutorial/challenges/re-group-groups

import re
m = re.search(r'([a-zA-Z0-9])\1+', input())
print(m.group(1) if m else -1)
