# http://www.hackerrank.com/challenges/pangrams

print('pangram' if len(set([c.lower() for c in input() if c.isalpha()])) == 26 else 'not pangram')
