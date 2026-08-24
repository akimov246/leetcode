package main

import "fmt"

func main() {
	fmt.Println(romanToInt("III"))
	fmt.Println(romanToInt("LVIII"))
	fmt.Println(romanToInt("MCMXCIV"))
}

var RtI = map[rune]int{
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}

func romanToInt(s string) int {
	runes := []rune(s)
	var result int

	var prev int
	for i := len(runes) - 1; i > -1; i-- {
		current := RtI[runes[i]]
		if current < prev {
			result -= current
		} else {
			result += current
		}
		prev = current
	}

	return result
}
