package main

import "fmt"

func main() {
	fmt.Println(hammingWeight(11))
	fmt.Println(hammingWeight(128))
	fmt.Println(hammingWeight(2147483645))
}

func hammingWeight(n int) int {
	weight := 0

	for n != 0 {
		weight++
		n &= (n - 1)
	}

	return weight
}
