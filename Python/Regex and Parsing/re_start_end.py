# http://www.hackerrank.com/contests/python-tutorial/challenges/re-start-re-end

import re
s = input()
k = input()
p = re.compile('(?=(' + k + '))')
if p.search(s):
    print(*[(m.start(1), m.end(1)-1) for m in p.finditer(s)], sep='\n')
else:
    print((-1, -1))
