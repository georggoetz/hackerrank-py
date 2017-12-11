# http://www.hackerrank.com/contests/python-tutorial/challenges/calendar-module

import datetime
import calendar

if __name__ == '__main__':
    m, d, y = map(int, input().split())
    print(calendar.day_name[datetime.date(y, m, d).weekday()].upper())
