# http://www.hackerrank.com/contests/python-tutorial/challenges/find-a-string


def count_substring(string, sub_string):
    start = num = 0
    while start >= 0:
        pos = string.find(sub_string, start)
        if pos < 0:
            break
        num += 1
        start = pos+1
    return num


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
