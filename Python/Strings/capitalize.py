# http://www.hackerrank.com/contests/python-tutorial/challenges/capitalize

import re


def capitalize(s):
    return re.sub(r'^[a-z]|(?<=\s)([a-z])', lambda m: m.group(0)[0].upper(), s)


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
