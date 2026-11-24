package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

func main() {
	fmt.Println(wordPattern("abba", "dog cat cat dog"))
	fmt.Println(wordPattern("abba", "dog cat cat fish"))
	fmt.Println(wordPattern("aaaa", "dog cat cat dog"))
	fmt.Println(wordPattern("abba", "dog dog dog dog"))
}

func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")
	if utf8.RuneCountInString(pattern) != len(words) {
		return false
	}
	patternRunes := []rune(pattern)
	runeToWord := make(map[rune]string)
	wordToRune := make(map[string]rune)
	for i := range patternRunes {
		word, wordExists := runeToWord[patternRunes[i]]
		r, rExists := wordToRune[words[i]]
		if (wordExists || rExists) && (word != words[i] || r != patternRunes[i]) {
			return false
		} else {
			runeToWord[patternRunes[i]] = words[i]
			wordToRune[words[i]] = patternRunes[i]
		}
	}
	return true
}
