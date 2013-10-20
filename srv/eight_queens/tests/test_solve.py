__author__ = 'jankrause'

import unittest2

from solve import solve_queens, no_conflict


class TestSolve(unittest2.TestCase):
    def test_solve_queens(self):
        expected = []

        for row in range(8):
            for column in range(8):
                expected.append({'row': row, 'column': column})

        self.assertEqual(solve_queens(), expected)

    def test_no_conflict(self):
        self.assertTrue(no_conflict(1,2,[]))


if __name__ == '__main__':
    unittest2.main()
