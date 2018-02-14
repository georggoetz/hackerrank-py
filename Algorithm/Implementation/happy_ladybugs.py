# http://www.hackerrank.com/challenges/happy-ladybugs

from collections import Counter


def make_happy():
    int(input())
    b = input()
    counter = Counter(b)
    if '_' not in counter:
        c = 1
        for i in range(1, len(b)):
            if b[i] == b[i-1]:
                c += 1
            else:
                if c == 1:
                    return 'NO'
                else:
                    c = 1
        return 'NO' if c == 1 else 'YES'
    for key in counter:
        if key != '_' and counter[key] == 1:
            return 'NO'
    return 'YES'


for _ in range(int(input())):
    print(make_happy())
