package main

import (
	"fmt"
)

func main() {
	fmt.Println(reverseBits(43261596))
	fmt.Println(reverseBits(2147483644))
}

func reverseBits(n int) int {
	result := 0
	for range 32 {
		result <<= 1
		result |= (n & 1)
		n >>= 1
	}
	return result
}
