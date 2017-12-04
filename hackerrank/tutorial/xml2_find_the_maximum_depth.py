# http://www.hackerrank.com/contests/python-tutorial/challenges/xml2-find-the-maximum-depth

import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    if elem is None:
        return
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
