# http://www.hackerrank.com/challenges/acm-icpc-team

from itertools import combinations


def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1
    return count


def acm_team(topics):
    pairs = combinations(topics, 2)
    max_topics = 0
    max_teams = 0
    for pair in pairs:
        sum_topics = count_set_bits(pair[0] | pair[1])
        if sum_topics > max_topics:
            max_topics = sum_topics
            max_teams = 1
        elif sum_topics == max_topics:
            max_teams += 1
    return [max_topics, max_teams]


if __name__ == "__main__":
    n, m = map(int, input().strip().split(' '))
    topics = []
    for _ in range(n):
        topics.append(int(input().strip(), 2))
    result = acm_team(topics)
    print('\n'.join(map(str, result)))
