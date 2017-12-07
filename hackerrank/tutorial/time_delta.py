#!/bin/python3

from datetime import datetime

TIMESTAMP_FMT = '%a %d %b %Y %H:%M:%S %z'


def time_delta(t1, t2):
    d1 = datetime.strptime(t1, TIMESTAMP_FMT)
    d2 = datetime.strptime(t2, TIMESTAMP_FMT)
    return int(abs(d1 - d2).total_seconds())


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
