# http://www.hackerrank.com/contests/python-tutorial/challenges/finding-the-percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = input()
    a = student_marks[query_name]
    print("{0:0.2f}".format(sum(a)/len(a)))
