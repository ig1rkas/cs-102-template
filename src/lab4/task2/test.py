import unittest
from main import SplitOnGroups


class TestFuncs(unittest.TestCase):
    def test_rec(self):
        self.assertEqual(SplitOnGroups().split_by_age([["Danya", "14"], ["Me", "25"]]), [['Danya (14)'], ['Me (25)']])
        self.assertEqual(SplitOnGroups().split_by_age([["Danya", "14"], ["Me", "25"], ["grand", "124"]]), [['Danya (14)'], ['Me (25)']])


if __name__ == "__main__":
    unittest.main()