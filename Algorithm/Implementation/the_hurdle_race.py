# http://www.hackerrank.com/challenges/the-hurdle-race

_, k = map(int, input().split())
print(max(0, max(map(int, input().split())) - k))
