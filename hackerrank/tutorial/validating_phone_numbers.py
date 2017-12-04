# http://www.hackerrank.com/contests/python-tutorial/challenges/validating-the-phone-number

import re

for i in range(int(input())):
    print('YES' if re.search(r'^[789]\d{9}$', input()) else 'NO')
