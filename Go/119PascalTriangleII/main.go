package main

import "fmt"

func main() {
	fmt.Println(getRow(3))
}

func getRow(rowIndex int) []int {
	dp := make([][]int, rowIndex+1)

	for i := range rowIndex + 1 {
		dp[i] = make([]int, i+1)
		dp[i][0], dp[i][i] = 1, 1
		for j := 1; j < i; j++ {
			dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
		}
	}
	return dp[rowIndex]
}
