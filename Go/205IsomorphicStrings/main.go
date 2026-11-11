package main

import (
	"fmt"
)

func main() {
	fmt.Println(isIsomorphic("egg", "add"))
	fmt.Println(isIsomorphic("f11", "b23"))
	fmt.Println(isIsomorphic("paper", "title"))
	fmt.Println(isIsomorphic("badc", "baba"))
}

func isIsomorphic(s string, t string) bool {
	sRunes := []rune(s)
	tRunes := []rune(t)
	sMap := make(map[rune]rune)
	tMap := make(map[rune]rune)

	for i := range len(sRunes) {
		sRune := sRunes[i]
		tRune := tRunes[i]

		if _, exists := sMap[sRune]; !exists {
			sMap[sRune] = tRune
		}

		if _, exists := tMap[tRune]; !exists {
			tMap[tRune] = sRune
		}

		if sMap[sRune] != tRune || tMap[tRune] != sRune {
			return false
		}
	}
	return true
}
