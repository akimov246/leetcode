package main

import "fmt"

func main() {
	fmt.Println(isUgly(6))
	fmt.Println(isUgly(1))
	fmt.Println(isUgly(14))
}

func isUgly(n int) bool {
	if n == 0 {
		return false
	}
	if n == 1 {
		return true
	}
	if n%2 == 0 {
		return isUgly(n / 2)
	}
	if n%3 == 0 {
		return isUgly(n / 3)
	}
	if n%5 == 0 {
		return isUgly(n / 5)
	}
	return false
}
