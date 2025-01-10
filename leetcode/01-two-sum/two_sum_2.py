# o(n^2)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for main_idx, main_item in enumerate(nums):
            for comp_idx, comp_item in enumerate(nums[main_idx+1:]):
                if main_item + comp_item == target:
                    return [main_idx, comp_idx+1+main_idx]
        