class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2
            mid = nums[mid_index]

            if mid == target:
                return mid_index
            
            if mid > target:
                right = mid_index - 1
            else:
                left = mid_index + 1

        return left