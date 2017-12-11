# http://www.hackerrank.com/contests/python-tutorial/challenges/string-validators

if __name__ == '__main__':
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False
    s = input()
    for c in s:
        if c.isalnum():
            isalnum = True
        if c.isalpha():
            isalpha = True
        if c.isdigit():
            isdigit = True
        if c.islower():
            islower = True
        if c.isupper():
            isupper = True
    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)
