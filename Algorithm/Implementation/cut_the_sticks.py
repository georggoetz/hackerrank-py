# http://www.hackerrank.com/challenges/cut-the-sticks


def cutTheSticks(arr):
    arr.sort()
    ans = []
    while len(arr) > 0:
        ans.append(len(arr))
        min = arr[0]
        j = 0
        for i in range(len(arr)):
            arr[i] -= min
            if arr[i] <= 0:
                j += 1
        arr = arr[j:]
    return ans


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = cutTheSticks(arr)
    print("\n".join(map(str, result)))
