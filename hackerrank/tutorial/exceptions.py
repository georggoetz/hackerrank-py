# http://www.hackerrank.com/contests/python-tutorial/challenges/exceptions

t = int(input())
for _ in range(t):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print('Error Code: ' + str(e))
