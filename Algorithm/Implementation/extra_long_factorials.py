# http://www.hackerrank.com/challenges/extra-long-factorials

if __name__ == "__main__":
    n = int(input().strip())
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)
