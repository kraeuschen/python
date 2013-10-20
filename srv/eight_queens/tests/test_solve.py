__author__ = 'jankrause'

import unittest2

from solve import solve_queens, no_conflict


class TestSolve(unittest2.TestCase):
    def test_no_conflict(self):
        self.assertTrue(no_conflict(1,2,[]))

        solutions = []
        solutions.append({'row': 0, 'column': 0});

        self.assertFalse(no_conflict(0,4, solutions))
        self.assertTrue(no_conflict(1,3, solutions))

        solutions = []
        solutions.append({'column': 0, 'row': 0})
        solutions.append({'column': 2, 'row': 1})
        solutions.append({'column': 4, 'row': 2})
        solutions.append({'column': 6, 'row': 3})

        self.assertTrue(no_conflict(4, 1, solutions))

        solutions = []
        solutions.append({'column': 0, 'row': 0})

        self.assertFalse(no_conflict(7, 7, solutions))

        solutions = []
        solutions.append({'column': 7, 'row': 7})

        self.assertFalse(no_conflict(0, 0, solutions))


if __name__ == '__main__':
    unittest2.main()
