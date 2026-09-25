package main

import (
	"fmt"
	"slices"
)

func main() {
	fmt.Println(plusOne([]int{1, 2, 3}))
	fmt.Println(plusOne([]int{4, 3, 2, 1}))
	fmt.Println(plusOne([]int{9}))
}

func plusOne(digits []int) []int {
	result := make([]int, len(digits)+1)

	for i, d := range digits {
		result[i+1] = d
	}

	result[len(result)-1]++

	for i := range slices.Backward(result) {
		if result[i] > 9 {
			result[i-1] += result[i] / 10
			result[i] %= 10
		}
	}

	if result[0] == 0 {
		return result[1:]
	}

	return result
}
