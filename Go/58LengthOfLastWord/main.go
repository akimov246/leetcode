package main

import (
	"fmt"
)

func main() {
	fmt.Println(lengthOfLastWord("Hello World"))
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
	fmt.Println(lengthOfLastWord("luffy is still joyboy"))
}

func lengthOfLastWord(s string) int {
	i := len(s) - 1

	for i >= 0 && s[i] == ' ' {
		i--
	}

	length := 0
	for i >= 0 && s[i] != ' ' {
		length++
		i--
	}

	return length
}
