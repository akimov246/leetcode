package main

import (
	"fmt"
)

func main() {
	fmt.Println(generate(5))
}

func generate(numRows int) [][]int {
	triangle := make([][]int, 0, numRows)
	for range numRows {
		n := len(triangle)
		newRow := make([]int, 0, n+1)
		for i := range n + 1 {
			switch i {
			case 0, n:
				newRow = append(newRow, 1)
			default:
				newRow = append(newRow, triangle[n-1][i-1]+triangle[n-1][i])
			}
		}
		triangle = append(triangle, newRow)
	}
	return triangle
}
