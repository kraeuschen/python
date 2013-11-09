__author__ = 'jankrause'

import unittest2

from solve import no_conflict


class TestSolve(unittest2.TestCase):
    def test_no_conflict(self):
        self.assertTrue(no_conflict(1,2,[]))

        solutions = [(0, 0)];

        self.assertFalse(no_conflict(0,4, solutions))
        self.assertTrue(no_conflict(1,3, solutions))

        solutions = [(0,0),(1,2),(2,4),(3,6)]

        self.assertTrue(no_conflict(4, 1, solutions))

        solutions = [(0, 0)]

        self.assertFalse(no_conflict(7, 7, solutions))

        solutions = [(7, 7)]

        self.assertFalse(no_conflict(0, 0, solutions))


if __name__ == '__main__':
    unittest2.main()
