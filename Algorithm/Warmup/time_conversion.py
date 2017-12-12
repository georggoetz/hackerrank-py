# http://www.hackerrank.com/challenges/time-conversion

from datetime import datetime


def timeConversion(s):
    return datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')


s = input().strip()
result = timeConversion(s)
print(result)
