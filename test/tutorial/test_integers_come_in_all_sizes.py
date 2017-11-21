import doctest
import unittest

from hackerrank.tutorial import integers_come_in_all_sizes


class Test(unittest.TestCase):

    def test_solve(self):
        doctest.testmod(integers_come_in_all_sizes)


if __name__ == "__main__":
    unittest.main()
