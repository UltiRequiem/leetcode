import unittest
from normal_python import Solution

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_target_not_found(self):
        self.assertEqual(self.solution.binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_empty_list(self):
        self.assertEqual(self.solution.binary_search([], 3), -1)

    def test_single_element_found(self):
        self.assertEqual(self.solution.binary_search([3], 3), 0)

    def test_single_element_not_found(self):
        self.assertEqual(self.solution.binary_search([1], 3), -1)

    def test_multiple_occurrences(self):
        self.assertEqual(self.solution.binary_search([1, 2, 3, 3, 3, 4, 5], 3), 2)

if __name__ == '__main__':
    unittest.main()
