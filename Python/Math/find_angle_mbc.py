# http://www.hackerrank.com/contests/python-tutorial/challenges/find-angle

import math

ab = int(input())
bc = int(input())
# hypotenuse
ac = math.sqrt(ab ** 2 + bc ** 2)
mc = ac / 2.0
# median
mb = math.sqrt(2.0 * (ab**2 + bc**2) - ac**2) / 2.0
theta = math.acos((mb**2 + bc**2 - mc**2) / (2.0 * mb * bc))
print(str(int(round(math.degrees(theta)))) + '°')
