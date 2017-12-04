# http://www.hackerrank.com/contests/python-tutorial/challenges/validate-a-roman-number

import re

str = input()
pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
match = re.search(pattern, str)
print('True' if match else 'False')
