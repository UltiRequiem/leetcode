from typing import List


class Solution:
  def binary_search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
      mid_index = (left + right) // 2 # floor
      mid_val = nums[mid_index]

      if mid_val == target:
        return mid_index
      
      if mid_val > target:
        right = mid_index - 1
      else: 
        left = mid_index + 1

    return -1
