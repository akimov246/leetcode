package main

import (
	"fmt"
	"slices"
)

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
	fmt.Println(isAnagram("rat", "car"))
	fmt.Println(isAnagram("ggii", "eekk"))
}

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	sRunes := []rune(s)
	tRunes := []rune(t)
	slices.Sort(sRunes)
	slices.Sort(tRunes)

	return slices.Equal(sRunes, tRunes)
}
