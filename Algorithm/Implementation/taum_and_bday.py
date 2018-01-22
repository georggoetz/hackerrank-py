# http://www.hackerrank.com/challenges/taum-and-bday


def taumBday(b, w, x, y, z):
    x = min(x, y + z)
    y = min(y, x + z)
    return b*x + w*y


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        b, w = map(int, input().strip().split(' '))
        x, y, z = map(int, input().strip().split(' '))
        result = taumBday(b, w, x, y, z)
        print(result)
