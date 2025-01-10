class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}

        for index, element in enumerate(nums):
            diff = target - element # target should be always bigger than element

            if diff in seen:
                return [index, seen[diff]]

            seen[element] = index # save index
        