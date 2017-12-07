# http://www.hackerrank.com/contests/python-tutorial/challenges/validating-postalcode

import re
inp = input().strip()
print(bool(re.match(r'^[1-9]\d{5}$', inp)) and len(re.findall(r'(\d)(?=(?:\d)(\1))', inp)) < 2)
