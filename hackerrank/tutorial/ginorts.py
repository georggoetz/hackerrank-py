# http://www.hackerrank.com/contests/python-tutorial/challenges/ginorts

print(*sorted(input(), key=lambda x: (not x.islower(), not x.isupper(), x.isdigit() and int(x) % 2 == 0, x)), sep='')
