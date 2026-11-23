package main

func main() {
	moveZeroes([]int{0, 1, 0, 3, 12})
}

func moveZeroes(nums []int) {
	i := 0
	for j := range nums {
		if nums[j] != 0 {
			nums[i] = nums[j]
			i++
		}
	}
	for j := i; j < len(nums); j++ {
		nums[j] = 0
	}
}
