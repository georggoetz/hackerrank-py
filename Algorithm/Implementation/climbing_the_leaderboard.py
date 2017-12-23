# http://www.hackerrank.com/challenges/climbing-the-leaderboard

if __name__ == "__main__":
    n = int(input().strip())
    scores = []
    for score in map(int, input().strip().split(' ')):
        if not scores or scores[-1] != score:
            scores.append(score)
    m = int(input().strip())
    rank = len(scores)
    for score in map(int, input().strip().split(' ')):
        while rank > 0 and scores[rank - 1] < score:
            rank -= 1
        print(rank if scores[rank - 1] == score else rank + 1)
