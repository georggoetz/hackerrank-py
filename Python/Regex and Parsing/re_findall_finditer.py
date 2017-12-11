# http://www.hackerrank.com/contests/python-tutorial/challenges/re-findall-re-finditer

import re
m = re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([aeiouAEIOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', input())
print(*m if m else [-1], sep='\n')
