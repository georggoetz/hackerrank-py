# http://www.hackerrank.com/contests/python-tutorial/challenges/xml-1-find-the-score

import xml.etree.ElementTree as etree


def read_input():
    n = int(input())
    xml = ''
    for _ in range(n):
        xml += input()
    return xml


def solve(xml):
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    return get_attr_number(root)


def get_attr_number(node):
    num = len(node.attrib)
    for child in node:
        num += get_attr_number(child)
    return num


if __name__ == "__main__":
    print(solve(read_input()))
