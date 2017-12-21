# http://www.hackerrank.com/challenges/day-of-the-programmer


def is_leap(year):
    if year < 2018:
        return year % 4 == 0
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0


def solve(year):
    dm = '13.09.'
    if year == 1918:
        dm = '26.09.'
    elif is_leap(year):
        dm = '12.09.'
    return dm + str(year)


year = int(input().strip())
result = solve(year)
print(result)
