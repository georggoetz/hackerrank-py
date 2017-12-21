# http://www.hackerrank.com/challenges/cats-and-a-mouse


q = int(input().strip())
for _ in range(q):
    x, y, z = map(int, input().strip().split(' '))
    a, b = abs(z - x), abs(z - y)
    if a > b:
        print('Cat B')
    elif a < b:
        print('Cat A')
    else:
        print("Mouse C")
