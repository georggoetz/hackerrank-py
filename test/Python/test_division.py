import doctest
import unittest
from hackerrank.tutorial import division


class Test(unittest.TestCase):

    def test_solve(self):
        doctest.testmod(division)


if __name__ == "__main__":
    unittest.main()
