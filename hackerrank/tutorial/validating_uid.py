# http://www.hackerrank.com/contests/python-tutorial/challenges/validating-uid

import re
p = r'(?=[a-zA-Z0-9]{10})(?=(.*[A-Z]){2})(?=(.*[0-9]){3})'
for _ in range(int(input())):
    inp = input().strip()
    print('Valid' if len(set(inp)) == 10 and re.match(p, inp) else 'Invalid')
