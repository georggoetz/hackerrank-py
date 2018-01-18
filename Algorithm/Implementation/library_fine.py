# https://www.hackerrank.com/challenges/library-fine

from datetime import date


def libraryFine(d1, m1, y1, d2, m2, y2):
    act = date(y1, m1, d1)
    due = date(y2, m2, d2)
    if act <= due:
        return 0
    if act.year > due.year:
        return 10000
    if act.month == due.month:
        return 15 * (act.day-due.day)
    else:
        return 500 * (act.month - due.month)


if __name__ == "__main__":
    d1, m1, y1 = map(int, input().strip().split(' '))
    d2, m2, y2 = map(int, input().strip().split(' '))
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)
