import doctest
import unittest

from hackerrank.tutorial import arithmetic_operators


class Test(unittest.TestCase):

    def test_solve(self):
        doctest.testmod(arithmetic_operators)


if __name__ == "__main__":
    unittest.main()
