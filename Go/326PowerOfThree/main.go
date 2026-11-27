package main

import (
	"fmt"
)

func main() {
	fmt.Println(isPowerOfThree(441))
}

func isPowerOfThree(n int) bool {
	const maxPow3 = 1162261467
	return n > 0 && maxPow3%n == 0
}
