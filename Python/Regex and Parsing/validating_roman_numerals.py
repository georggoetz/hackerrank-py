# http://www.hackerrank.com/contests/python-tutorial/challenges/validate-a-roman-number

import re

str = input()
pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print(bool(re.search(pattern, str)))
