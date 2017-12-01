# http://www.hackerrank.com/contests/python-tutorial/challenges/decorators-2-name-directory

from operator import itemgetter


def person_lister(f):
    def inner(people):
        ans = []
        for person in sorted(people, key=itemgetter(2)):
            ans.append(f(person))
        return ans
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
