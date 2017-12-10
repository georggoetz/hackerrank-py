# http://www.hackerrank.com/challenges/py-if-else

if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0:
        print('Weird')
    else:
        print('Weird' if n >= 6 and n <= 20 else 'Not Weird')
