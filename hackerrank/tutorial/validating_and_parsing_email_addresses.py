# http://www.hackerrank.com/contests/python-tutorial/challenges/validating-named-email-addresses

import email.utils
import re

for _ in range(int(input())):
    inp = input()
    addr = email.utils.parseaddr(inp)
    if re.match(r'^[A-Za-z]{1}[A-Za-z0-9_\.-]*@[A-Za-z]+\.[A-Za-z]{1,3}$', addr[1]):
        print(inp)
