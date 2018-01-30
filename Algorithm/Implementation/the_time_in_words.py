# http://www.hackerrank.com/challenges/the-time-in-words

words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'quarter',
    16: 'sixteen',
    17: 'seventeen',
    19: 'nineteen',
    20: 'twenty',
    21: 'twenty one',
    22: 'twenty two',
    23: 'twenty three',
    24: 'twenty four',
    25: 'twenty five',
    26: 'twenty six',
    27: 'twenty seven',
    28: 'twenty eight',
    29: 'twenty nine',
    30: 'half'
}

h = int(input().strip())
m = int(input().strip())

if m == 0:
    print(words[h] + ' o\' clock')
else:
    s = 'past'
    if m > 30:
        m = 60 - m
        h += 1
        h %= 12
        s = 'to'
    if m == 15 or m == 30:
        s = words[m] + ' ' + s
    elif m == 1:
        s = words[m] + ' minute ' + s
    else:
        s = words[m] + ' minutes ' + s
    print(s + ' ' + words[h])
