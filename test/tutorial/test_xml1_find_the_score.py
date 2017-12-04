import unittest
from hackerrank.tutorial.find_the_score import solve

sample = """
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>"""


class TestFindTheScore(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_attr_number(self):
        self.assertEqual(solve(sample), 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
