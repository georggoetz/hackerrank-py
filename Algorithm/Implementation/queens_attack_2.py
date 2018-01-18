# http://www.hackerrank.com/challenges/queens-attack-2

if __name__ == "__main__":
    n, k = map(int, input().split())
    rq, cq = map(int, input().split())

    top = n - rq
    bottom = rq - 1
    left = cq - 1
    right = n - cq
    top_left = min(top, left)
    top_right = min(top, right)
    bottom_left = min(bottom, left)
    bottom_right = min(bottom, right)

    for _ in range(k):
        r, c = map(int, input().split())

        new_top = r - rq - 1
        new_bottom = rq - r - 1
        new_left = cq - c - 1
        new_right = c - cq - 1
        new_top_left = min(new_top, new_left)
        new_top_right = min(new_top, new_right)
        new_bottom_left = min(new_bottom, new_left)
        new_bottom_right = min(new_bottom, new_right)

        # vertical
        if c == cq:
            # top
            if r > rq:
                top = min(top, new_top)
            # bottom
            elif r < rq:
                bottom = min(bottom, new_bottom)

        # horizontal
        if r == rq:
            # right
            if c > cq:
                right = min(right, new_right)
            # left
            elif c < cq:
                left = min(left, new_left)

        # diagonal
        if abs(rq - r) == abs(cq - c):
            if r > rq:
                # top_left
                if c < cq:
                    top_left = min(top_left, new_top_left)
                # top_right
                elif c > cq:
                    top_right = min(top_right, new_top_right)
            elif r < rq:
                # bottom_left
                if c < cq:
                    bottom_left = min(bottom_left, new_bottom_left)
                # bottom_right
                elif c > cq:
                    bottom_right = min(bottom_right, new_bottom_right)

    print(sum([top, bottom, left, right, top_left, top_right, bottom_left,
               bottom_right]))
