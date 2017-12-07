# http://www.hackerrank.com/contests/python-tutorial/challenges/validating-credit-card-number

import re
match = r'^[456](\d{15}|\d{3}(-\d{4}){3})$'
search = r'(\d)\1\1\1'
for _ in range(int(input())):
    inp = input().strip()
    m = re.match(match, inp)
    s = re.search(search, inp.replace('-', ''))
    print('Valid' if m and not s else 'Invalid')
