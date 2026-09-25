package main

import (
	"fmt"
	"slices"
)

func main() {
	fmt.Println(addBinary("11", "1"))
	fmt.Println(addBinary("1010", "1011"))
}

func addBinary(a string, b string) string {
	var result []byte
	carry := 0
	i := len(a) - 1
	j := len(b) - 1

	for i >= 0 || j >= 0 || carry > 0 {
		sum := 0
		if i >= 0 {
			sum += int(a[i])
			i--
		}
		if j >= 0 {
			sum += int(b[j])
			j--
		}
		sum += carry

		result = append(result, byte('0'+sum%2))
		carry = sum / 2 % 2
	}

	slices.Reverse(result)
	return string(result)
}
