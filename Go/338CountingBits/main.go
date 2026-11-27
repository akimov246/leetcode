package main

import "fmt"

func main() {
	fmt.Println(countBits(5))
}

func countBits(n int) []int {
	ans := make([]int, 0, n+1)
	for i := range n + 1 {
		counter := 0
		for i != 0 {
			counter++
			i &= (i - 1)
		}
		ans = append(ans, counter)
	}
	return ans
}
