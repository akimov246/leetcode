package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {
	fmt.Println(longestCommonPrefix([]string{"flower", "flow", "flight"}))
	fmt.Println(longestCommonPrefix([]string{"dog", "racecar", "car"}))
}

func longestCommonPrefix(strs []string) string {
	currentLength := math.MaxInt
	for _, word := range strs {
		currentLength = min(len(word), currentLength)
	}

outer:
	for currentLength > 0 {
		prefix := strs[0][:currentLength]
		for _, word := range strs {
			if !strings.HasPrefix(word, prefix) {
				currentLength--
				continue outer
			}
		}
		return prefix
	}
	return ""
}
