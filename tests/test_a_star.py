import unittest

from a_star import AStarHeuristics
from taquin import Taquin


class AStarTestsHelper:
    # items is a list of list where each sublist represents a line
    @staticmethod
    def prepare_taquin_for_test(items):
        taq = Taquin()
        for j in range(taq.n):
            for i in range(taq.n):
                if items[i][j] == 0:
                    taq.empty_slot = (j, i)
                taq.board_numbers[(j, i)] = items[i][j]
        return taq


class AStarTests(unittest.TestCase):
    def setUp(self):
        self.taq1 = AStarTestsHelper.prepare_taquin_for_test([[7, 2, 4], [5, 0, 6], [8, 3, 1]])
        self.taq2 = AStarTestsHelper.prepare_taquin_for_test([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.taq3 = AStarTestsHelper.prepare_taquin_for_test([[8, 7, 6], [5, 4, 3], [2, 1, 0]])

    def test_h1(self):
        self.assertEqual(8, AStarHeuristics.h1(self.taq1))
        self.assertEqual(0, AStarHeuristics.h1(self.taq2))
        self.assertEqual(7, AStarHeuristics.h1(self.taq3))

    def test_h2(self):
        self.assertEqual(18, AStarHeuristics.h2(self.taq1))
        self.assertEqual(0, AStarHeuristics.h2(self.taq2))
        self.assertEqual(20, AStarHeuristics.h2(self.taq3))
