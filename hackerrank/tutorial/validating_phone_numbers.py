# http://www.hackerrank.com/contests/python-tutorial/challenges/validating-the-phone-number

import re

n = int(input())
for i in range(n):
    str = input()
    match = re.search(r'^[789]\d{9}$', str)
    print('YES' if match else 'NO')
