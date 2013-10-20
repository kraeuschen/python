__author__ = 'jankrause'

import unittest2

from solve import solve_queens


class TestSolve(unittest2.TestCase):
    def test_solve_queens(self):
        expected = []
        self.assertEqual(solve_queens(), expected)


if __name__ == '__main__':
    unittest2.main()
