# http://www.hackerrank.com/contests/python-tutorial/challenges/polar-coordinates

import cmath

if __name__ == '__main__':
    z = complex(input())
    print(abs(z))
    print(cmath.phase(z))
