package main

import (
	"fmt"
	"slices"
)

func main() {
	fmt.Println(containsDuplicate([]int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}))
}

func containsDuplicate(nums []int) bool {
	slices.Sort(nums)
	for i := range len(nums) - 1 {
		if nums[i] == nums[i+1] {
			return true
		}
	}
	return false
}
