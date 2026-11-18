package main

import (
	"fmt"
)

func main() {
	fmt.Println(isPowerOfTwo(1))
	fmt.Println(isPowerOfTwo(16))
	fmt.Println(isPowerOfTwo(3))
	fmt.Println(isPowerOfTwo(8))
}

func isPowerOfTwo(n int) bool {
	return n > 0 && (n&(n-1)) == 0
}
