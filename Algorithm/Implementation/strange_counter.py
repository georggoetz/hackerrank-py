# http://www.hackerrank.com/challenges/strange-code

t = int(input())
rem = 3
while rem < t:
    t = t - rem
    rem *= 2
print(rem-t+1)
