# http://www.hackerrank.com/contests/python-tutorial/challenges/most-commons

from collections import Counter

if __name__ == "__main__":
    s = sorted(Counter(input().strip()).most_common(), key=lambda x: (-x[1], x[0]))[:3]
    for letter, count in s:
        print(' '.join([letter, str(count)]))
