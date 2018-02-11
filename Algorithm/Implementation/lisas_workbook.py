# http://www.hackerrank.com/challenges/lisa-workbook

n, k = map(int, input().split())
t = list(map(int, input().split()))
page = 1
special = 0
for chapter in range(1, n + 1):
    chapter_page = 1
    for problem in range(1, t[chapter - 1] + 1):
        if problem > chapter_page * k:
            page += 1
            chapter_page += 1
        if problem == page:
            special += 1
    page += 1
print(special)
