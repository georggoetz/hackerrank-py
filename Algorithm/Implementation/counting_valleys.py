# http://www.hackerrank.com/challenges/counting-valleys

n = int(input())
steps = input()
height = 0
is_in_valley = False
valley_count = 0
for step in steps:
    if step == 'U':
        height += 1
    if step == 'D':
        height -= 1
    if height == -1 and not is_in_valley:
        is_in_valley = True
    if height == 0 and is_in_valley:
        is_in_valley = False
        valley_count += 1
print(valley_count)
