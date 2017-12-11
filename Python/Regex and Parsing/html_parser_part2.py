# http://www.hackerrank.com/contests/python-tutorial/challenges/html-parser-part-2

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        lines = data.split('\n')
        print('>>> ' + ('Multi-line Comment' if len(lines) > 1 else 'Single-line Comment'))
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)

        
if __name__ == '__main__':
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
