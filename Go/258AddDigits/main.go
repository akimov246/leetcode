package main

import (
	"fmt"
)

func main() {
	fmt.Println(addDigits(38))
}

func addDigits(num int) int {
	return 1 + ((num - 1) % 9)
}
