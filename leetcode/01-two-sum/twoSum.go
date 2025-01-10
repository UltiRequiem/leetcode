package main

func twoSum(nums []int, target int) []int {
    memo := make(map[int]int)

    for index, num := range nums {
        if val, exists := memo[target-num]; exists {
            return []int {val, index}
        }

        memo[num] = index
    }

    return nil
}