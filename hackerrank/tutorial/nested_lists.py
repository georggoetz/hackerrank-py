# http://www.hackerrank.com/contests/python-tutorial/challenges/nested-list

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    s = sorted(set(map(lambda x: x[1], students)))[1]
    print('\n'.join(sorted(list(map(lambda x: x[0], list(filter(lambda x: x[1] == s, students)))))))
