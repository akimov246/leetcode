package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(summaryRanges([]int{0, 1, 2, 4, 5, 7}))
	fmt.Println(summaryRanges([]int{0, 2, 3, 4, 6, 8, 9}))
}

func summaryRanges(nums []int) []string {
	ranges := make([]string, 0)

	i := 0
	for i < len(nums) {
		start := i

		for i+1 < len(nums) && nums[i+1] == nums[i]+1 {
			i++
		}

		if start == i {
			ranges = append(ranges, strconv.Itoa(nums[i]))
		} else {
			ranges = append(ranges, strconv.Itoa(nums[start])+"->"+strconv.Itoa(nums[i]))
		}
		i++
	}
	return ranges
}
