# http://www.hackerrank.com/challenges/grading


def solve(grades):
    result = []
    for grade in grades:
        d = 5 - grade % 5
        result.append(grade if grade < 38 or d >= 3 else grade + d)
    return result


grades = []
for _ in range(int(input().strip())):
    grades.append(int(input().strip()))
print('\n'.join(map(str, solve(grades))))
