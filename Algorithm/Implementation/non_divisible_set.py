# http://www.hackerrank.com/challenges/non-divisible-subse


def nonDivisibleSubset(k, arr):
    # Count residue classes
    residues = [0] * k
    for n in arr:
        residues[n % k] += 1

    # There can be only one element in the result set with n%k = 0
    count = min(residues[0], 1)

    # If k is even only one of the equal remainders can be added to the result
    # set.
    # E.g. k = 6, 1 + 5, 2 + 4, 3 + 3. Value three can only be counted once.
    if k % 2 == 0:
        count += 1

    #   For any number k, the sum of 2 numbers (a+b) is divisible by k if the
    # sum of the remainders of a%k + b%k is k.
    #   For any k the possible remainders are 0, 1,... k-1
    #   For any such remainder there is only one remainder that makes the sum
    # divisible by k.
    #   E.g. k = 5 the remainder pairs are 1 + 4 and 2 + 3
    #   Therefore, choose the larger set of each pair
    i, j = 1, len(residues)-1
    while i < j:
        count += max(residues[i], residues[j])
        i += 1
        j -= 1

    return count


if __name__ == "__main__":
    n, k = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)
