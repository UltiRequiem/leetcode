import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [1, 0])

    def test_no_solution(self):
        self.assertIsNone(self.solution.twoSum([1, 2, 3], 7))

    def test_multiple_solutions(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5], 6), [3, 1])

    def test_negative_numbers(self):
        self.assertEqual(self.solution.twoSum([-1, -2, -3, -4, -5], -8), [4, 2])

    def test_mixed_numbers(self):
        self.assertEqual(self.solution.twoSum([-1, 2, 3, -4, 5], 1), [4, 0])

if __name__ == '__main__':
    unittest.main()
