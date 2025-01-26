#include <vector>

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right){
            int mid = (right + left) / 2;
            int num = nums[mid];

            if (num == target){
                return mid;
            }

            if (target < num){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1;
    }
};