import unittest
from lp_calculator import estimate_games


class EstimateTests(unittest.TestCase):
    def test_positive_progress(self):
        self.assertEqual(estimate_games(500, 600, 0.6), 25)

    def test_no_progress(self):
        self.assertIsNone(estimate_games(500, 600, 0.5))
        self.assertIsNone(estimate_games(500, 600, 0.4))

    def test_target_reached(self):
        self.assertEqual(estimate_games(600, 500, 0.4), 0)

    def test_rounds_up(self):
        self.assertEqual(estimate_games(0, 21, 1), 2)

    def test_invalid_inputs(self):
        for values in [(0, 100, 1.1), (0, 100, -0.1),
                       (0, float("nan"), 0.6), (0, 100, 0.6, 0)]:
            with self.subTest(values=values), self.assertRaises(ValueError):
                estimate_games(*values)


if __name__ == "__main__":
    unittest.main()
