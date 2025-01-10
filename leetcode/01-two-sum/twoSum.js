/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const memo = {};

  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];

    if (diff in memo) {
      return [i, memo[diff]];
    }

    memo[nums[i]] = i;
  }
};
