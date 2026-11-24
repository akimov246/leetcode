package main

import "fmt"

func main() {
	numArray := Constructor([]int{-2, 0, 3, -5, 2, -1})
	fmt.Println(numArray.SumRange(0, 2))
	fmt.Println(numArray.SumRange(2, 5))
	fmt.Println(numArray.SumRange(0, 5))
}

type NumArray struct {
	prefix []int
}

func Constructor(nums []int) NumArray {
	prefix := make([]int, len(nums)+1)
	for i, n := range nums {
		prefix[i+1] = prefix[i] + n
	}
	return NumArray{prefix: prefix}
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.prefix[right+1] - this.prefix[left]
}
