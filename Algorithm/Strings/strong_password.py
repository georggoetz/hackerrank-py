# http://www.hackerrank.com/challenges/strong-password

n = int(input())
pw = list(input())
specials = '!@#$%^&*()-+'
has_digit = False
has_lower_char = False
has_upper_char = False
has_special = False
for c in pw:
    if c.isdigit():
        has_digit = True
    elif c.isalpha() and c.islower():
        has_lower_char = True
    elif c.isalpha() and c.isupper():
        has_upper_char = True
    elif specials.find(c) >= 0:
        has_special = True
count = 4
if has_digit:
    count -= 1
if has_lower_char:
    count -= 1
if has_upper_char:
    count -= 1
if has_special:
    count -= 1
print(max(count, 6 - len(pw)))
