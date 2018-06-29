#!/bin/python3

n, s, k = int(input()), str(input()), int(input())
result = ''
for c in s:
    shift = ord('a') if c.islower() else ord('A')
    result += chr((ord(c) - shift + k)%26 + shift) if c.isalpha() else c
print(result)
