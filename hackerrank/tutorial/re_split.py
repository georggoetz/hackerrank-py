# http://www.hackerrank.com/contests/python-tutorial/challenges/re-split

import re
print('\n'.join(filter(None, re.split('[,.]+', input()))))
