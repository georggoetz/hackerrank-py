# http://www.hackerrank.com/contests/python-tutorial/challenges/the-minion-game


def minion_game(string):
    n = len(string)
    kevin = stuart = 0
    for i in range(n):
        if string[i] in 'AEIOU':
            kevin += n-i
        else:
            stuart += n-i
    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print('Kevin ' + str(kevin))
    else:
        print('Stuart ' + str(stuart))


if __name__ == '__main__':
    s = input()
    minion_game(s)
