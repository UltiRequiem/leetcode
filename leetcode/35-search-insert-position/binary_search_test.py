import unittest
from binary_search import Solution

class TestSearchInsert(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)

    def test_insert_position(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 2), 1)

    def test_insert_at_end(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 7), 4)

    def test_insert_at_start(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 0), 0)

    def test_empty_list(self):
        self.assertEqual(self.solution.searchInsert([], 5), 0)

if __name__ == '__main__':
    unittest.main()
