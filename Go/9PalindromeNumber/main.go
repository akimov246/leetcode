package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(isPalindrome(121))
}

func isPalindrome(x int) bool {
	str := strconv.Itoa(x)
	return str == reverse(str)
}

func reverse(s string) string {
	var result string
	for _, rune := range s {
		result = string(rune) + result
	}
	return result
}
