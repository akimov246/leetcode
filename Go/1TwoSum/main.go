package main

import (
	"fmt"
)

func main() {
	//fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(twoSum([]int{3, 2, 4}, 6))
}

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)

	for i, value := range nums {
		if j, ok := seen[target-value]; ok {
			return []int{i, j}
		}
		seen[value] = i
	}

	return nil
}
