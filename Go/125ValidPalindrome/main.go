package main

import (
	"fmt"
	"unicode"
)

func main() {
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
	fmt.Println(isPalindrome("race a car"))
	fmt.Println(isPalindrome(" "))
}

func isPalindrome(s string) bool {
	l := 0
	r := len(s) - 1

	for l <= r {
		leftLower := unicode.ToLower(rune(s[l]))
		rightLower := unicode.ToLower(rune(s[r]))

		if !(unicode.IsLower(leftLower) || unicode.IsDigit(leftLower)) {
			l++
			continue
		}

		if !(unicode.IsLower(rightLower) || unicode.IsDigit(rightLower)) {
			r--
			continue
		}

		if leftLower != rightLower {
			return false
		}
		l++
		r--
	}

	return true
}
