# http://www.hackerrank.com/contests/python-tutorial/challenges/word-order

if __name__ == '__main__':
    words = []
    countOf = {}
    for _ in range(int(input())):
        word = input()
        if word in countOf:
            countOf[word] += 1
        else:
            countOf[word] = 1
            words.append(word)
    print(len(countOf))
    print(' '.join(str(countOf[word]) for word in words))
