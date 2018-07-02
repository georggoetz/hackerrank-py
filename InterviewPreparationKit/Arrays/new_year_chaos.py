# http://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D=interview-preparation-kit&slugs%5B%5D=arrays

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (n+1)
    chaos = False
    # Bubblesort
    while (True):
        swapped = False
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
                swapped = True
                if c[a[i]] == 2:
                    swapped = False
                    chaos = True
                    break
                else:
                    c[a[i]] += 1
        if not swapped:
            break
    print('Too chaotic' if chaos else sum(c))
