# http://www.hackerrank.com/challenges/designer-pdf-viewer

h = list(map(int, input().strip().split(' ')))
word = input().strip()
print(h[ord(max(word, key=lambda letter: h[ord(letter)-97]))-97] * len(word))
