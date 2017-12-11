
# http://www.hackerrank.com/contests/python-tutorial/challenges/detect-html-tags-attributes-and-attribute-values

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.print_attrs(attrs)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        self.print_attrs(attrs)

    def print_attrs(self, attrs):
        for name, value in attrs:
            print('-> ' + name + ' > ' + (value if value else 'None'))


if __name__ == '__main__':
    html = ''
    for i in range(int(input())):
        html = html + input() + '\n'
    parser = MyHTMLParser()
    parser.feed(html)
