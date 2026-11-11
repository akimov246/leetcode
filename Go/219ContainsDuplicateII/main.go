package main

import "fmt"

func main() {
	fmt.Println(containsNearbyDuplicate([]int{1, 2, 3, 1, 2, 3}, 2))
}

func containsNearbyDuplicate(nums []int, k int) bool {
	m := make(map[int]int, len(nums))

	for j, n := range nums {
		if i, exists := m[n]; exists {
			if j-i <= k {
				return true
			}
		}
		m[n] = j
	}
	return false
}
