package main

import "fmt"

func main() {
	fmt.Println(removeElement([]int{3, 2, 2, 3}, 3))
	fmt.Println(removeElement([]int{0, 1, 2, 2, 3, 0, 4, 2}, 2))
}

func removeElement(nums []int, val int) int {
    k := 0
	for _, num := range nums {
		if num != val {
			nums[k] = num
			k++
		}
	}
	return k
}
