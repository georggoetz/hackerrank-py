# http://www.hackerrank.com/challenges/beautiful-binary-string

_ = int(input())
s = input()
i = s.find('010')
count = 0
while i != -1:
    i = s.find('010', i+3)
    count += 1
print(count)
