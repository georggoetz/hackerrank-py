# http://www.hackerrank.com/contests/python-tutorial/challenges/python-tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
