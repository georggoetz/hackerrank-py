# http://www.hackerrank.com/challenges/mars-exploration/problem

s = input()
sos = 'SOS'

result = 0
for i in range(len(s)):
    c = s[i]
    if c != sos[i % 3]:
        result += 1
print(result)
