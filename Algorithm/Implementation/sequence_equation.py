# http://www.hackerrank.com/challenges/permutation-equation

if __name__ == "__main__":
    n = int(input().strip())
    p = [0] * (n+1)
    for i, v in enumerate(map(int, input().split())):
        p[v] = i+1
    for i in range(1, n+1):
        print(p[p[i]])
