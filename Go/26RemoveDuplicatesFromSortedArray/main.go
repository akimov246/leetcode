package main

import "fmt"

func main() {
	fmt.Println(removeDuplicates([]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}))
}

func removeDuplicates(nums []int) int {
	visited := make(map[int]bool)
	
	for _, value := range nums {
		if !visited[value] {
			visited[value] = true
		}
	}
	fmt.Println(visited)
	return len(visited)
}
